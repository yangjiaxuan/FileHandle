#!/usr/local/bin/Python3
#encoding=utf-8
import os
import json


fileUrl = os.getcwd() + "/a.json"

def createFile(filename):
    if not os.path.exists(filename):
        fp = open(filename, 'w+') # 创建文件
        fp.close()# 关闭
        print("创建新的文件:%s"%filename)

def removeFile(filename):
    if os.path.exists(filename):
        os.remove(filename)


#本方法尽可以设置一次，不能重复设置，新设备的内容会覆盖旧内容
def saveDictionaryAsJsonString(filename, contents):
    
    removeFile(fileUrl)
    createFile(fileUrl)
    
    fh = open(filename, 'w')
    json_str = json.dumps(contents)
    fh.write(json_str)
    fh.close()

# 向文件中追加一行 contents必须为字符串
def addNewLine(filename, contents):
    
    createFile(fileUrl)
    fp = open(filename, 'a')
    fp.write("\r\n")
    fp.write(contents)
    fp.close()


