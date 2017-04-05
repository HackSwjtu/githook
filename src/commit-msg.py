#!/usr/bin/env python

import sys, os, re
from subprocess import check_output

commit_msg_filepath = sys.argv[1]

branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
print("commit-msg: On branch '%s'" % branch)
