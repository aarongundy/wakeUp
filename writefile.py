# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:57:51 2013

@author: aaron
"""

def writeAlarmData(alarmList):
    f = open("alarmdata","w")
    for i in range(len(alarmList)):
        for j in range(4):
			if j< 2:
				f.write(str(alarmList[i][j])+"|")
			if j ==2:
				f.write(str(alarmList[i][j][0])+":"+str(alarmList[i][j][1])+"|")
			if j == 3:
				f.write(alarmList[i][j])
        f.write("\n")
    f.close()

if __name__ == "__main__":
	alarm = [['True', 'School', '6:09', 'wkdys'],['False', 'Alarm1', '8:05', 'mon']]
	writeAlarmData()
