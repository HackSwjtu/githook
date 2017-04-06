#!/bin/sh

if git rev-parse --verify HEAD >/dev/null 2>&1 then
    echo "pre-commit: About to create a new commit..."
    against=HEAD
else
    echo "pre-commit: About to create the first commit..."
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

echo "pre-commit: Testing for whitespace errors..."
if ! git diff-index --check --cached $against then
    echo "pre-commit: Aborting commit due to whitespace errors"
    exit 1
else 
    echo "pre-commit: No whitespace errors : "
    exit 0
fi
