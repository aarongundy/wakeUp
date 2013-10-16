# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:36:20 2013

@author: aaron
"""
def readAlarmData():
    alarmList = []
    count = 0
    f = open("alarmdata")

    for line in f:
        line = line.strip()
        # line = line.replace(" ", "")
        alarmList.append((line.split("|",4)))
        alarmList[count][2]= alarmList[count][2].split(":")
        alarmList[count][2][0]= int(alarmList[count][2][0])
        alarmList[count][2][1]= int(alarmList[count][2][1])
        if not line:break
        # print alarmList[count]
        count += 1
    
    f.close()

    return alarmList

if __name__ == "__main__":
	alarmList = []
	readAlarmData()