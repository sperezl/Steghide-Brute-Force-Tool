#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from progressbar import ProgressBar, Percentage, Bar
from argparse import ArgumentParser
import subprocess
import os


class color:
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    BLUE2 = '\033[1;36m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[1;32m'

SAMPLE = """
Type ./steg_brute.py -h to show help

Command line example:
    Brute force attack with dictionary to
       extract hide info of file
    ./steg_brute.py -d <dictionary> -f <file>
    """


def stegBrute(inputFile, dictionary):
    i = 0
    outputFile = inputFile.split('.')[0] + "_flag.txt"
    lines = len(open(dictionary).readlines())
    with open(dictionary, 'r') as passFile:
        for line in passFile.readlines():
            password = line.strip('\n')
            result = subprocess.run(["steghide", "--extract", "-sf", inputFile, "-p", password, "-xf", outputFile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            if result is 0:
                print("\n\n [+] Information obtained with password: {} \n ".format(password))
                break

def main():
    argp = ArgumentParser()
    argp.add_argument('-f', '--file', dest='file', required=True,
                      help='Path of file')

    argp.add_argument('-d', '--dictionary', dest='dictionary',
                      help='Path of dictionary to brute force attack')

    args = argp.parse_args()

    if args.file and args.dictionary:
        print("\n [i] " + color.INFO + "Attempting..." + color.ENDC)
        stegBrute(args.file, args.dictionary)

    else:
        print(SAMPLE)


if __name__ == "__main__":
    main()
