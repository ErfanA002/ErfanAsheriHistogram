#!/bin/bash

# Read the commit message from the temporary file
COMMIT_MSG=$(cat "$1")

# Check the commit message using regex
if [[ ! "$COMMIT_MSG" =~ ^(feat|fix|docs|style|refactor|test|chore)(\([a-z]+\))?:\s.+ ]]; then
  echo "Error: Commit message does not follow Gitflow conventions."
  echo "Please use one of the following formats:"
  echo "  - feat(scope): description"
  echo "  - fix(scope): description"
  echo "  - docs(scope): description"
  echo "  - style(scope): description"
  echo "  - refactor(scope): description"
  echo "  - test(scope): description"
  echo "  - chore(scope): description"
  exit 1
fi

exit 0