#!/usr/bin/env python

# Cleans the static code analysis report.
import re
import glob
import os
import datetime
import calendar

authorFooter = '''AUTHORSTART %(author)s AUTHORSTOP DATESTART %(date)s DATESTOP PAGESTART %(authorpage)s PAGESTOP'''
files = glob.glob("../doc/tutorials/*")
for file in files:
    with open(file) as f: content = f.read()

    authorPattern = re.compile(r'.*@author (\w+ \w*)', re.MULTILINE|re.DOTALL)
    datePattern = re.compile(r'.*date (\d+-\d+-\d+) .*', re.MULTILINE|re.DOTALL)

    date = datePattern.match(content)
    author = authorPattern.match(content)

    author = author.groups()[0] if author else "Unknown"
    date = date.groups()[0] if date else "None"

    for line in content.splitlines():
        if "@date" in line:
            content = content.replace(line, '')
            break;

    dateInfo = date.split("-")
    year = "0000"
    month = "Unknown"
    day = "00"
    if len(dateInfo) == 3:
        year = dateInfo[0]
        month = calendar.month_name[int(dateInfo[1])]
        day = dateInfo[2]

    dateContent = authorFooter % {'author' : author,
                                  'date' : day + " " + month + " " + year,
                                  'authorpage' : author.replace(" ", "") + "Page"}

    with open(file, "w") as f:
        f.write(content + "\n")
        f.write(dateContent)
