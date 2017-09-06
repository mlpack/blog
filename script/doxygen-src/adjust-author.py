#!/usr/bin/env python

# Cleans the static code analysis report.
import re
import glob
import os
import datetime
from time import strptime
import argparse


def adjustAuthor(files):
    authorHeader = '''
    <div align="right">
        <span class="mlabel" style="border: 0px solid #333333;">
            <a href="%(authorpage)s.html" style="color:#ffffff !important">%(author)s, %(date)s</a>
        </span>
    </div>'''

    for htmlFile in files:
        with open(htmlFile) as f: content = f.read()

        authorPattern = re.compile('.*AUTHORSTART (.*) AUTHORSTOP.*', re.MULTILINE|re.DOTALL)
        datePattern = re.compile('.*DATESTART (.*) DATESTOP.*', re.MULTILINE|re.DOTALL)
        pagePattern = re.compile('.*PAGESTART (.*) PAGESTOP.*', re.MULTILINE|re.DOTALL)

        author = authorPattern.match(content)
        date = datePattern.match(content)
        page = pagePattern.match(content)

        if author and date and page:
            author = author.groups()[0]
            date = date.groups()[0]
            page = page.groups()[0]

            authorStartPos = content.find("AUTHORSTART")
            pageStopPos = content.find("PAGESTOP")
            metaInfo = content[authorStartPos:pageStopPos + len("PAGESTOP")]

            # Remove temporary meta data.
            content = content.replace(metaInfo, "")

            # Add author information.
            authorContent = authorHeader % {'author' : author,
                                            'date' : date,
                                            'authorpage' : page}
            content = content.replace("</h1>", "</h1>" + authorContent, 1)

            with open(htmlFile, "w") as f:
                f.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Adjust the author.""")
    parser.add_argument('-p','--path', help='Path to generated html files.', required=True)

    args = parser.parse_args()
    if args:
        if args.path.endswith("/"):
            path = args.path + "*.html"
        else:
            path = args.path + "/*.html"

        files = glob.glob(path)
        adjustAuthor(files)
