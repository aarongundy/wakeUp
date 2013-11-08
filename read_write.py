#Read_write
from alarmclass import *

def readAlarmData():
    alarmList = []
    f = open("alarmdata")

    for line in f:
        line = line.strip()
        new_alarm = line.split("|",4)
        enabled = new_alarm[0]
        name = new_alarm[1]
        time= new_alarm[2].split(":")
        hour= int(time[0])
        minute = int(time[1])
        days = new_alarm[3]
        new_alarm = Alarm(enabled,name,hour,minute,days)
        alarmList.append(new_alarm)
        if not line:break
    
    f.close()

    return alarmList

def writeAlarmData(alarmList):
    f = open("alarmdata","w")
    for i in range(len(alarmList)):
    	alarm_p = alarmList[i]
    	f.write(str(alarm_p.enabled)+"|"+alarm_p.name+"|"+str(alarm_p.hour)+":"+str(alarm_p.minute)+"|"+alarm_p.days+"\n")
    f.close()

if __name__ == "__main__":
	pass