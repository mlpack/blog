#!/usr/bin/env python

# Cleans the static code analysis report.
import re
import glob
import os
import datetime
from time import strptime
import argparse

def lastPosts(files, number):
    lastFiles = []
    dates = {}
    datesContent = ""
    for htmlFile in files:
        with open(htmlFile) as f: content = f.read()

        datePattern = re.compile('.*By .*, (.*)</a></div>.*', re.MULTILINE|re.DOTALL)
        pagePattern = re.compile(r'.*page ([\w+-]*).*', re.MULTILINE|re.DOTALL)

        date = datePattern.match(content)
        page = pagePattern.match("\n".join(content.split("\n")[:4]))

        if date and page:
            date = date.groups()[0]

            if "Unknown" in date:
                continue;

            page = page.groups()[0]

            dateKey = date.split(" ", )
            dateKey = dateKey[0] + " " \
                + str(strptime(dateKey[1][:3],'%b').tm_mon) + " " + dateKey[2]

            if dateKey in dates:
                dates[dateKey].append(page)
            else:
                dates[dateKey] = [page]

    dateKeys = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d %m %Y'), reverse=True)

    i = 0
    for dateKey in dateKeys:
        for page in dates[dateKey]:
            if i < number:
                lastFiles.append("blog/doxygen/" + page + ".html")
            i = i + 1

    return lastFiles

def extractContent(htmlFile):
    with open(htmlFile) as f: content = f.read()

    r = re.compile('.*<div class="header">(.+)<hr class="footer"></hr><address class="footer"><small >.*', re.MULTILINE|re.DOTALL)
    m = r.match(content)
    if m:
        extContent = '<div class="header">' + m.groups()[0]
        extContent = extContent.replace('<div class="textblock"><h1 >', '<div class="textblock"><h1 style="color:#bb2222">')
        return extContent

    return ""

def insertContent(htmlFile, htmlContent):
    with open(htmlFile) as f: content = f.read()

    rStart = re.compile('(.*)<div class="contents">.*', re.MULTILINE|re.DOTALL)
    rStop = re.compile('.*<hr class="footer"></hr><address class="footer"><small >(.*)', re.MULTILINE|re.DOTALL)

    start = rStart.match(content)
    stop = rStop.match(content)
    if start and stop:
        contentStart = start.groups()[0] + '<div class="contents">'
        contentStop = '<div> <hr class="footer"></hr><address class="footer"><small >' + stop.groups()[0]

        with open(htmlFile, "w") as f:
            f.write(contentStart)
            f.write(htmlContent)
            f.write(contentStop)

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
        files = lastPosts(files, 12)

        content = ""

        for i in range(len(files)):
            content = content + extractContent(files[i])
            if i < (len(files) - 1):
                content = content + '<div class="directory"></div>'

        indexFile = "blog/doxygen/index.html"
        insertContent(indexFile, content)

