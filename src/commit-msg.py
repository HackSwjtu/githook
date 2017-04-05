#!/usr/bin python

import sys, os, re
from subprocess import check_output

commit_msg_filepath = sys.argv[1]

branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
print("commit-msg: On branch '%s'" % branch)

if branch.startswith('issue-'):
    print('commit-msg: Oh hey, it\'s an issue branch')
    result = re.match('issue-(.*)', branch)
    issue_number = result.group(1)
    required_message = "ISSUE-%s" % issue_number

    with open(commit_msg_filepath, 'r') as f:
        content = f.read()
        if not content.startswith(required_message):
            print("commit-msg: ERROR! The commit message must start with '%s'" % required_message)
            sys.exit(1)
