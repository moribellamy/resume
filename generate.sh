#!/usr/bin/env bash

OUTPUT=${1:-resume.html}

hackmyresume BUILD resume.json TO $OUTPUT -t node_modules/jsonresume-theme-elegant
