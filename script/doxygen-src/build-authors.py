#!/usr/bin/env python

# Cleans the static code analysis report.
import re
import glob
import os
import datetime
import argparse
from shutil import copyfile

def insertContent(htmlFile, htmlContent):
    with open(htmlFile) as f: content = f.read()

    rStart = re.compile('(.*)<div class="contents">.*', re.MULTILINE|re.DOTALL)
    rStop = re.compile('.*<hr class="footer"></hr><address class="footer"><small >(.*)', re.MULTILINE|re.DOTALL)

    start = rStart.match(content)
    stop = rStop.match(content)
    if start and stop:
        contentStart = start.groups()[0] + '<div class="contents"><div class="textblock">Here is a list of all authors.</div><div class="directory"><table class="directory">'
        contentStop = '</table><div><div> <hr class="footer"></hr><address class="footer"><small >' + stop.groups()[0]

        with open(htmlFile, "w") as f:
            f.write(contentStart)
            f.write(htmlContent)
            f.write(contentStop)

def extractContent(files):
    authorHeader = '''
    <tr class="even" id="row_%(row)s_">
        <td class="entry">
        <span style="width:0px;display:inline-block;">&#160;</span>
        <span class="arrow" onclick="toggleFolder('%(row)s_')">&#9660;</span>
        <a class="el" href="%(authorpage)s.html">%(author)s</a></td>
    </tr>'''

    article = '''
    <tr id="row_%(row)s_%(rowID)s_" style="display:%(display)s;">
      <td class="entry">
        <span style="width:32px;display:inline-block;">&#160;</span>
            <span class="icona"><span class="icon">%(id)s</span>
        </span>
        <a class="el" href="%(page)s.html">%(brief)s</a>
      </td>
      <td class="desc">%(date)s</td>
    </tr>'''

    authorContent = {}
    authorsContent = ""
    authors = {}
    for htmlFile in files:
        with open(htmlFile) as f: content = f.read()
        authorPattern = re.compile('.*By (.*),.*', re.MULTILINE|re.DOTALL)
        pagePattern = re.compile(r'.*page ([\w+-]*).*', re.MULTILINE|re.DOTALL)
        brief = re.compile('.*@brief (.*).*', re.MULTILINE)

        author = authorPattern.match(content)
        page = pagePattern.match("\n".join(content.split("\n")[:4]))
        brief = brief.match(content)

        if author and page and brief:
            author = author.groups()[0]
            page = page.groups()[0]
            brief = brief.groups()[0]

            # Truncate brief.
            brief = (brief[:75] + ' ..') if len(brief) > 75 else brief


            date = datetime.datetime.fromtimestamp(
                os.path.getmtime(htmlFile)).strftime('%Y-%m-%d')

            if author in authors:
                authors[author].append((page, brief, date))
            else:
                authors[author] = [(page, brief, date),]
    row = 0
    for author, info in authors.items():
        authorContent[author] = authorHeader % {'author' : author,
                                                'row' : str(row),
                                                'authorpage' : author.replace(" ", "") + "Page",} + "\n"
        authorsContent = authorsContent + authorContent[author]

        i = 1
        for page, brief, date in info:
            articleContentNone = article % {'id' : str(i),
                                        'page' : page,
                                        'brief' : brief,
                                        'row' : str(row),
                                        'rowID' : str(i),
                                        'display' : 'none',
                                        'date' : "",}

            articleContentDisplay = article % {'id' : str(i),
                                        'page' : page,
                                        'brief' : brief,
                                        'row' : str(row),
                                        'rowID' : str(i),
                                        'display' : 'table-row',
                                        'date' : "",}

            authorsContent = authorsContent + articleContentNone + "\n"
            authorContent[author] = authorContent[author] + articleContentDisplay + "\n"

            i = i + 1
        row = row + 1

    return authorsContent, authorContent

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
        content, authorContent = extractContent(files)

        indexFile = "blog/doxygen/authors.html"

        for author, info in authorContent.items():
            authorFile = os.path.dirname(indexFile) + "/" + author.replace(" ", "") + "Page.html"
            copyfile(indexFile, authorFile)
            insertContent(authorFile, info)

        insertContent(indexFile, content)
