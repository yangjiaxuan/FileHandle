#!/usr/local/bin/Python3
#encoding=utf-8
import sys
import os
import FileHandle


fileUrl = os.getcwd() + "/a.json"

def createParam(appKey, appSecret, BaseURL, asrURL):
    param = {'appKey': appKey,
             'appSecret': appSecret,
             'BaseURL': BaseURL,
             'asrURL': asrURL}

    FileHandle.saveDictionaryAsJsonString(fileUrl, param)
    print (param)


def main(appKey, appSecret, BaseURL, asrURL):
    createParam(appKey, appSecret, BaseURL, asrURL)

main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

