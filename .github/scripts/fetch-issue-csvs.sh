#!/usr/bin/env bash
# Download CSV attachments from a GitHub issue and print as plain text.
#
# Usage:
#   ./fetch-issue-csvs.sh --issue 1201                        # by issue number
#   ./fetch-issue-csvs.sh --label metrics                      # latest open issue with label
#   ./fetch-issue-csvs.sh --label metrics --drop-columns "Post text,Post Link"
#
# Options:
#   --issue NUM          Specific issue number
#   --label LABEL        Find latest open issue with this label
#   --drop-columns COLS  Comma-separated columns to remove (default: "Post text")
#   --top N              Keep only top N rows by first numeric column (default: 0 = all)
#
# Scans issue body + all comments for github.com/user-attachments CSV URLs,
# downloads each, drops specified columns, optionally keeps only top rows.

set -euo pipefail

REPO="${GITHUB_REPOSITORY:-AICMO/Autonomous-Agent-X-Bluesky}"
ISSUE=""
LABEL=""
DROP_COLUMNS="Post text"
TOP_N=0

while [[ $# -gt 0 ]]; do
  case $1 in
    --issue) ISSUE="$2"; shift 2 ;;
    --label) LABEL="$2"; shift 2 ;;
    --drop-columns) DROP_COLUMNS="$2"; shift 2 ;;
    --top) TOP_N="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

# Resolve issue number
if [ -z "$ISSUE" ] && [ -n "$LABEL" ]; then
  ISSUE=$(gh issue list --repo "$REPO" --label "$LABEL" --state open --limit 1 --json number --jq '.[0].number // empty')
fi

if [ -z "$ISSUE" ]; then
  echo "No issue found"
  exit 0
fi

echo "Scanning issue #${ISSUE} for CSV attachments" >&2

# Collect CSV URLs from issue body and comments
BODY_URLS=$(gh issue view "$ISSUE" --repo "$REPO" --json body --jq '.body' \
  | grep -oE 'https://github\.com/user-attachments/files/[^ )]+\.csv' || true)

COMMENT_URLS=$(gh api "repos/${REPO}/issues/${ISSUE}/comments" --jq '.[].body' \
  | grep -oE 'https://github\.com/user-attachments/files/[^ )]+\.csv' || true)

URLS=$(printf '%s\n%s' "$BODY_URLS" "$COMMENT_URLS" | grep -v '^$' | sort -u)

if [ -z "$URLS" ]; then
  echo "No CSV attachments in issue #${ISSUE}" >&2
  exit 0
fi

# Download and print each CSV
while IFS= read -r url; do
  FILENAME=$(basename "$url" | python3 -c "import sys,urllib.parse; print(urllib.parse.unquote(sys.stdin.read().strip()))")
  echo "Downloading: ${FILENAME}" >&2
  CONTENT=$(curl -sL "$url")
  if [ -n "$CONTENT" ]; then
    echo ""
    echo "=== ${FILENAME} ==="
    echo "$CONTENT" | python3 -c "
import csv, sys

drop = [c.strip() for c in '''${DROP_COLUMNS}'''.split(',') if c.strip()]
top_n = ${TOP_N}

reader = csv.DictReader(sys.stdin)
if not reader.fieldnames:
    sys.exit(0)
keep = [f for f in reader.fieldnames if f not in drop]

rows = list(reader)
total = len(rows)

if top_n > 0 and total > top_n:
    # Sort by Impressions if present, else first numeric column
    sort_col = None
    if 'Impressions' in keep:
        sort_col = 'Impressions'
    else:
        for f in keep:
            try:
                float(rows[0].get(f, '').strip() or '0')
                sort_col = f
                break
            except ValueError:
                pass
    if sort_col:
        rows.sort(key=lambda r: float(r.get(sort_col, '0').strip() or '0'), reverse=True)
        rows = rows[:top_n]
        print(f'# Showing top {top_n}/{total} by {sort_col}', file=sys.stderr)

writer = csv.DictWriter(sys.stdout, fieldnames=keep, extrasaction='ignore')
writer.writeheader()
for row in rows:
    writer.writerow(row)
"
  fi
done <<< "$URLS"