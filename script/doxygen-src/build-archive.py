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
        <span style="width:32px;height:20px;display:inline-block;">&#160;</span>
            <span class="mlabel" style="border: 0px solid #333333;">
                <a href="%(authorpage)s.html" style="color:#ffffff !important">%(author)s</a>
            </span>
        </span>
        <a class="el" href="%(page)s.html">%(brief)s</a>
      </td>
      <td class="desc"></td>
    </tr>'''

    dates = {}
    datesContent = ""
    for htmlFile in files:
        with open(htmlFile) as f: content = f.read()

        authorPattern = re.compile('.*AUTHORSTART (.*) AUTHORSTOP.*', re.MULTILINE|re.DOTALL)
        datePattern = re.compile('.*DATESTART (.*) DATESTOP.*', re.MULTILINE|re.DOTALL)
        pagePattern = re.compile(r'.*page ([\w+-]*).*', re.MULTILINE|re.DOTALL)
        briefPattern = re.compile('.*@brief (.*)\n.*', re.MULTILINE)
        authorPagePattern = re.compile('.*PAGESTART (.*) PAGESTOP.*', re.MULTILINE|re.DOTALL)

        date = datePattern.match(content)
        page = pagePattern.match("\n".join(content.split("\n")[:4]))
        brief = briefPattern.match(content)
        author = authorPattern.match(content)
        authorPage = authorPagePattern.match(content)

        if date and page and brief and author and authorPage:
            date = date.groups()[0]

            if "Unknown" in date:
                continue;

            page = page.groups()[0]
            brief = brief.groups()[0]
            author = author.groups()[0]
            authorPage = authorPage.groups()[0]

            # Truncate brief.
            brief = (brief[:70] + ' ..') if len(brief) > 70 else brief

            dateKey = date.split(" ", )
            dateKey = dateKey[0] + " " \
                + str(strptime(dateKey[1][:3],'%b').tm_mon) + " " + dateKey[2]

            if dateKey in dates:
                dates[dateKey].append((page, brief, date, author, authorPage))
            else:
                dates[dateKey] = [(page, brief, date, author, authorPage),]

    dateKeys = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d %m %Y'), reverse=True)

    for dateKey in dateKeys:

        info = dates[dateKey]
        datesContent = datesContent + dateHeader % {'date' : info[0][2],}
        for page, brief, date, author, authorPage in info:
            datesContent = datesContent + article % {'author' : author,
                                                     'authorpage' : authorPage,
                                                     'page' : page,
                                                     'brief' : brief,}

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
