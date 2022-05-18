import json
import os
import pandas as pd
from pandas.io.json import json_normalize

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('max_colwidth', 200)

def read_reportContent():
    """读取日报信息"""
    # file = open('../data/0426','r',encoding='utf-8')
    # data = file.read()
    fileRead=''
    (CBStime,ACTtime,ERPtime) = (0,0,0)
    with open('../data/0426','r',encoding='utf-8') as f:
        while True:
            fileRead = f.readline()
            # print(fileRead)
            if fileRead.find('核心系统(CBS)')>0:
                print('核心系统(CBS)')
                print('起批时间：', f.readline().strip().replace(' ','').replace('\n',''))
                print('完成时间：', f.readline().strip().replace(' ','').replace('\n',''))
                exectueTime = f.readline()
                CBStime = stripTime(exectueTime)
                print('批量执行时间', CBStime,'分钟')
            if fileRead.find('会计引擎(ACT)')>0:
                print('会计引擎(ACT)')
                print('起批时间：', f.readline().strip().replace(' ','').replace('\n','').replace('【关账】',''))
                print('完成时间：', f.readline().strip().replace(' ','').replace('\n',''))
                exectueTime = f.readline()
                ACTtime = stripTime(exectueTime)
                print('批量执行时间', ACTtime,'分钟')
            if fileRead.find('总账境内(ERP)')>0:
                print('核心系统(CBS)')
                print('起批时间：', f.readline().strip().replace(' ','').replace('\n',''))
                print('完成时间：', f.readline().strip().replace(' ','').replace('\n',''))
                exectueTime = f.readline()
                ERPtime = stripTime(exectueTime)
                print('批量执行时间', ERPtime,'分钟')
            if not fileRead:
                break
    return CBStime, ACTtime, ERPtime

def stripTime(str):
    str=str.strip().replace(' ','').replace('\n','')
    if str.find('时') > 0:
        time = []
        time = str
        hour = int(time[0])
        minute = int(time[3:].replace('分钟', ''))
        timeTaken = hour*60+minute
        return (timeTaken)
    else:
        time = str
        minute = int(time.replace('分钟', ''))
        timeTaken = minute
        return (timeTaken)

a,b,c = read_reportContent()
print(a,b,c)