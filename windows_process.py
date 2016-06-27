#!/usr/bin/env python
import subprocess
import csv
import sys
p_tasklist = subprocess.Popen('tasklist.exe /fo csv',
                              stdout=subprocess.PIPE,
                              universal_newlines=True)

pythons_tasklist = []
for p in csv.DictReader(p_tasklist.stdout):
    if p['Image Name'] == 'WINDOWS PROCESS HERE':
        sys.exit(0)

sys.exit (2)
