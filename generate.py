#!/usr/bin/env python3

import os
import subprocess
import sys


# For web display. Inserts GA code.
def write_modified_website(output):
    subprocess.check_call([
        'node_modules/hackmyresume/dist/cli/index.js',
        'BUILD',
        'resume.json',
        'TO',
        output,
        '-t',
        'node_modules/jsonresume-theme-elegant'
    ])

    resume = open(output, 'r').read()
    ga = open('head.html', 'r').read()

    resume = resume.replace('<head>', '<head>\n' + ga)

    with open(output, 'w') as ofile:
        ofile.write(resume)


# For PDF conversion. Must do manually with chrome.
def write_html_for_pdf(output):
    base, ext = os.path.splitext(output)
    target = '%s-pdf%s' % (base, ext)
    subprocess.check_call([
        'node_modules/hackmyresume/dist/cli/index.js',
        'BUILD',
        'resume.json',
        'TO',
        target,
        '-t',
        'node_modules/jsonresume-theme-onepage'
    ])


if __name__ == '__main__':
    output = 'resume.html' if len(sys.argv) == 1 else sys.argv[1]
    write_modified_website(output)
    write_html_for_pdf(output)
