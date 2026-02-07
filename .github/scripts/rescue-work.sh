#!/usr/bin/env bash
# rescue-work.sh - Rescue unpushed work when agent hits max turns or fails
#
# Creates a PR from any uncommitted/unpushed work so it's not lost.
# Runs as a safety net after agent step failure.
#
# Required env vars:
#   GH_TOKEN - GitHub token for PR creation

set -euo pipefail

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Stage any uncommitted changes
git add -A
if ! git diff --staged --quiet; then
  git commit -m "[Agent] Rescued: uncommitted work from failed session"
fi

# Check if we're on a branch with unpushed commits
BRANCH=$(git branch --show-current)
if [ "$BRANCH" = "main" ]; then
  # Agent never created a branch — create one
  BRANCH="agent/rescue-$(date -u +%Y%m%d-%H%M%S)"
  git checkout -b "$BRANCH"
fi

# Check if there's anything to push (ahead of origin/main)
AHEAD=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo "0")
if [ "$AHEAD" -eq 0 ]; then
  echo "No unpushed work to rescue"
  exit 0
fi

git push -u origin "$BRANCH"

# Create PR if one doesn't exist for this branch
EXISTING=$(gh pr list --head "$BRANCH" --json number --jq length)
if [ "$EXISTING" -eq 0 ]; then
  PR_URL=$(gh pr create \
    --title "[Agent] Rescued: work from failed session" \
    --body "Agent hit max turns or failed before creating a PR. This rescues the work.")
  for i in 1 2 3; do
    gh pr merge "$PR_URL" --merge --delete-branch && break
    echo "Merge attempt $i failed, retrying in 5s..."
    sleep 5
  done
fi
