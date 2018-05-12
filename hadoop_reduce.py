#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys

def hadoopReduce(inputStream):
    wordCount = {}
    for line in inputStream:
        word , count = line.strip().split("\t")
        wordCount[word] = wordCount.get(word , 0) + int(count)
    for k , v in wordCount.items():
        print("%s\t%d" % (k , v))

if __name__ == '__main__':
    hadoopReduce(sys.stdin)
