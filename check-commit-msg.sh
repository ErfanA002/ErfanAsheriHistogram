#!/bin/bash

# دریافت پیام کامیت از فایل موقت
COMMIT_MSG=$(cat "$1")

# الگوی regex برای پیام‌های کامیت Gitflow (قابل تنظیم)
# مثال: feat(user-authentication): Add login feature
REGEX="^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)\(\w+\): .*$"

# بررسی مطابقت پیام با الگو
if [[ ! "$COMMIT_MSG" =~ $REGEX ]]; then
  echo "Error: Commit message does not follow Gitflow conventions."
  echo "Please use a format like: <type>(<scope>): <message>"
  echo "Example: feat(user-authentication): Add login feature"
  exit 1
fi

# اگر همه چیز درست بود
exit 0