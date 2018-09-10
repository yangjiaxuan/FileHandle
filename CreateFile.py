#!/usr/local/bin/Python3
#encoding=utf-8
import sys
import os
import FileHandle


fileUrl = os.getcwd() + "/b.h"

def createFile(need):
    if need:
        FileHandle.addNewLine(fileUrl, "#define kType true")
    else:
        FileHandle.addNewLine(fileUrl, "#define kType false")


def main(need):
    createFile(need)

main(sys.argv[1])

