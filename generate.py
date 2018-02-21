#!/usr/bin/env python3

import subprocess
import sys


def main():
    output = 'resume.html' if len(sys.argv) == 1 else sys.argv[1]

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


if __name__ == '__main__':
    main()
