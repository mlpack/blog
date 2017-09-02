#!/usr/bin/env python

# Cleans the static code analysis report.
import re
import glob
import os
import datetime
from shutil import copyfile
from time import strptime
import argparse

def insertContent(htmlFile, htmlContent):
    with open(htmlFile) as f: content = f.read()

    rStart = re.compile('(.*)<div class="contents">.*', re.MULTILINE|re.DOTALL)
    rStop = re.compile('.*<hr class="footer"></hr><address class="footer"><small >(.*)', re.MULTILINE|re.DOTALL)

    start = rStart.match(content)
    stop = rStop.match(content)
    if start and stop:
        contentStart = start.groups()[0] + '<div class="contents"><div class="textblock">Here is a list of all posts.</div><div class="directory"><table class="directory">'
        contentStop = '</table><div><div> <hr class="footer"></hr><address class="footer"><small >' + stop.groups()[0]

        with open(htmlFile, "w") as f:
            f.write(contentStart)
            f.write(htmlContent)
            f.write(contentStop)

def extractContent(files):
    dateHeader = '''
    <tr class="even">
        <td class="entry">
        <span style="width:0px;display:inline-block;">&#160;</span>
        <span class="arrow" onclick="toggleFolder(&apos;0_&apos;)">&#9660;</span>
        <a class="el"">%(date)s</a></td>
    </tr>'''

    article = '''
    <tr>
      <td class="entry">
        <span style="width:32px;display:inline-block;">&#160;</span>
            <span class="icona"><span class="icon">%(id)s</span>
        </span>
        <a class="el" href="%(page)s.html">%(brief)s</a>
      </td>
    </tr>'''

    dates = {}
    datesContent = ""
    for htmlFile in files:
        with open(htmlFile) as f: content = f.read()

        datePattern = re.compile('.*By .*, (.*)</a></div>.*', re.MULTILINE|re.DOTALL)
        pagePattern = re.compile(r'.*page ([\w+-]*).*', re.MULTILINE|re.DOTALL)
        brief = re.compile('.*@brief (.*)\n.*', re.MULTILINE)

        date = datePattern.match(content)
        page = pagePattern.match("\n".join(content.split("\n")[:4]))
        brief = brief.match(content)

        if date and page and brief:
            date = date.groups()[0]

            if "Unknown" in date:
                continue;

            page = page.groups()[0]
            brief = brief.groups()[0]

            # Truncate brief.
            brief = (brief[:75] + ' ..') if len(brief) > 75 else brief

            dateKey = date.split(" ", )
            dateKey = dateKey[0] + " " \
                + str(strptime(dateKey[1][:3],'%b').tm_mon) + " " + dateKey[2]

            if dateKey in dates:
                dates[dateKey].append((page, brief, date))
            else:
                dates[dateKey] = [(page, brief, date),]

    dateKeys = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d %m %Y'), reverse=True)

    for dateKey in dateKeys:

        info = dates[dateKey]
        datesContent = datesContent + dateHeader % {'date' : info[0][2],}
        i = 1
        for page, brief, date in info:
            datesContent = datesContent + article % {'id' : str(i),
                                                     'page' : page,
                                                     'brief' : brief,}
            i = i + 1

    return datesContent

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Builds the archive page.""")
    parser.add_argument('-p','--path', help='Path to tutorials.', required=True)

    args = parser.parse_args()
    if args:
        if args.path.endswith("/"):
            path = args.path + "*"
        else:
            path = args.path + "/*"

        files = glob.glob(path)
        content = extractContent(files)

        indexFile = "blog/doxygen/pages.html"
        insertContent(indexFile, content)
