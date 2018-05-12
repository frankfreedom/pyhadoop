#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys


def hadoopMap(inputStream):
    for line in inputStream:
        for word in line.strip().split():
            print("%s\t%d" % (word, 1))

if __name__ == '__main__':
    hadoopMap(sys.stdin)
