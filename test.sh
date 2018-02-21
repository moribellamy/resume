#!/usr/bin/env bash

./generate.py resume-test.html
if [[ $? -ne 0 ]]; then
    echo "Could not run generation script."
    exit 1
fi

diff resume.html resume-test.html
if [[ $? -ne 0 ]]; then
    echo "Checked in resume does not match resume.json."
    exit 1
fi

grep -q @@@ resume-test.html
if [[ $? -eq 0 ]]; then
	echo "Test failed, '@@@' is not present in Mori's resume :)."
	exit 1
fi
