#!/usr/bin/python3

'''
Create data from list of LZMA compressed archives of comments
Copyright 2016 Xiang Zhang

Usage: python3 create_data.py -i [input file pattern] -o [output file]
'''

import argparse
import csv
import glob
import json
import lzma

INPUT = '../data/jd/comment/*.json.xz'
OUTPUT = '../data/jd/sentiment/comment.csv'

def main():
    global INPUT
    global OUTPUT

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input', help = 'Input file pattern', default = INPUT)
    parser.add_argument(
        '-o', '--output', help = 'Output file', default = OUTPUT)

    args = parser.parse_args()

    INPUT = args.input
    OUTPUT = args.output

    createData()

def createData():
    # Open the output file
    ofd = open(OUTPUT, 'w', newline = '', encoding = 'utf-8')
    writer = csv.writer(ofd, quoting = csv.QUOTE_ALL, lineterminator = '\n')
    # Grab the files
    files = glob.glob(INPUT)
    n = 0
    filecount = 0
    for filename in files:
        filecount = filecount + 1
        print('Processing file {}/{}: {}. Processed items {}.'.format(
                filecount, len(files), filename, n))
        try:
            ifd = lzma.open(filename, 'rt', encoding = 'utf-8')
            for line in ifd:
                review = json.loads(line)
                score = int(review['content'].get('score', -1))
                title = review['content'].get('title', '')
                content = review['content'].get('content', '')
                if score != -1:
                    n = n + 1
                    writer.writerow([score, title.replace('\n', '\\n'),
                                     content.replace('\n', '\\n')])
            ifd.close()
        except Exception as e:
            print('Exception (ignored): {}'.format(e))
    ofd.close()

if __name__ == '__main__':
    main()
