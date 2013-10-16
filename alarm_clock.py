#!/usr/bin/python

# Alarm clock

#Add function that converts weekdays to multiple days after an event

from time import localtime
import datetime
from optparse import OptionParser
import readin
import alarmthreading
import writefile

def viewAlarms(alarmList):
    print ("")

    print ("Enabled\t Name\t      Time\tDays")
    print ("---------------------------------------")

    if len(alarmList)>=1:
        length = int(len(alarmList))
        #print length
        #print alarmList
        for i in range(length):
            print "", alarmList[i][0]," ", alarmList[i][1]," "*abs((12-len(alarmList[i][1]))),"%2s:%2s"%(str(alarmList[i][2][0]).zfill(2),str(alarmList[i][2][1]).zfill(2)),"   ",alarmList[i][3],""
        print ""
    else:
        print ("The alarm array is empty")

#Find all alarms that are turned on and print them to the console
def showActiveAlarms(alarmList):
    print

    enabled = []
    for alarm in alarmList:
        if alarm[0] == True:
            enabled.append(alarm)
    viewAlarms(enabled)

def onOff(alarmList):
    viewAlarms(alarmList)
    print
    while True:
        change = raw_input("Enter the name of the alarm you would like to toggle on or off").strip()
        for alarm in alarmList:
            if alarm[1] ==change:
                if alarm[0] == 'True':
                    alarm[0] == 'False'
                    print "You turned off alarm %s" %alarm[1]
                else:
                    alarm[0] == 'True'
                    print "You turned on alarm %s" %alarm[1]

def nextAlarm(alarmList):
    today = datetime.datetime.today().weekday()
    todaysAlarms = []

    print "Today is day:",today
    #See what alarms that are in the array are happening today and are enabled
    for alarm in alarmList:
        if alarm[0]== 'True':
            # print alarm
            if today == 0 and alarm[3] == 'mon' or alarm[3] == 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 1 and alarm[3] == 'tues' or alarm[3] == 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 2 and alarm[3] == 'wed' or alarm[3] == 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 3 and alarm[3] == 'thurs' or alarm[3] == 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 4 and alarm[3] == 'fri' or alarm[3] == 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 5 and alarm[3] == 'sat' or alarm[3] == 'wknds':
                todaysAlarms.append(alarm)
            elif today == 6 and alarm[3] == 'sun' or alarm[3] == 'wknds':
                todaysAlarms.append(alarm)
    # print todaysAlarms
    if len(todaysAlarms)>0:
        next_alarm = [todaysAlarms[0][0],todaysAlarms[0][1]]
        for alarm in todaysAlarms:
            if alarm[2][0]< next_alarm[0] and alarm[2][1]< next_alarm[1]:
                next_alarm = alarm[2]
            #Start the thread that watches the time
        alarmThread = alarmthreading.AlarmClockTimer(next_alarm[0],next_alarm[1],"bomb_siren.wav")
        alarmThread.start()

            # if alarm[3] == 'mon' and today == 0:
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")
            # if alarm[3] == 'tues' and today == 1:
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")
            # elif alarm[3] =='wkdys' and today >= 0 and today<= 4:
            #     # print "wkdys"
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")

def newAlarm():
    print
    name = raw_input("Enter the name of the alarm: ")
    alarmtime = inputTime()
    schedule = inputDays()
    print "You created a new alarm:",(name)
    print"Time: %2s:%2s"%(str(alarmtime[0]).zfill(2),str(alarmtime[1]).zfill(2))
    print (schedule)
    alarmList.append([True,name,alarmtime,schedule])
    print viewAlarms(alarmList)
    writefile.writeAlarmData(alarmList)
    # nextAlarm(alarmList)
    return

def inputTime():
    #alarmtime = alarmtime.split(":",2)
    while True:
        alarmtime = raw_input("Enter the time: ")
        alarmtime = alarmtime.split(":")
        alarmtime[0] = int(alarmtime[0])
        alarmtime[1] = int(alarmtime[1])
        if alarmtime[0]>= 0 and alarmtime[0]<=23:
            if alarmtime[1]>=0 and alarmtime[1]<=59:
                break
        else:
            print "**Please enter a valid time in 24 hour format**"
    return alarmtime

def inputDays():
    print ("Enter the days it will run: ")
    print ("\n_______Days of the Week________")
    print ("\n'sun' = Sunday")
    print ("'mon' = Monday")
    print ("'tues' = Tuesday")
    print ("'wed' = Wednesday")
    print ("'thurs' = Thursday")
    print ("'fri' = Friday")
    print ("'sat' = Saturday")
    print ("\n_______Intelligent Days________")
    print ("\n'wkdys' = Weekdays")
    print ("'wknds' = Weekends"   )

    schedule = raw_input("Enter the days it will run: ")
    return schedule

#def printOptions():


#parser = OptionParser()
#parser.add_option("-v","-viewall",help="Shows all the alarms",action="callback",callback=viewAlarms())
#(options, args) = parser.parse_args()

#________Begin Program____________
if __name__ == "__main__":
    alarmList = readin.readAlarmData()
    alarmtime = str
    name = str
    schedule = str
    print ""

    print "*"*40
    
    print ("     Welcome to the Alarm Clock")

    print "*"*40
    
    print

    time_now = localtime()
    
    print ("Current system time is: " + str(time_now.tm_hour).zfill(2) + ":" + str(time_now.tm_min).zfill(2))

    #alarmThread = alarmthreading()
    # alarmthreading.alarm.start()
    print ""
    print viewAlarms(alarmList)

    run = True

    while run == True:
        nextAlarm(alarmList)
        mode = raw_input("Enter a mode: ").strip()

        mode = mode.lower()

        try:
            if mode == "quit" or mode == 'q':
                print ("Bye!")
                raw_input()
                alarmthreading.AlarmClockTimer("","","").stop()
                run = False
            elif mode == 'view' or mode == 'v':
                viewAlarms(alarmList)
            # elif mode == "help":
                # printOptions()
            elif mode == "n":
                newAlarm()
                writefile.writeAlarmData(alarmList)
            elif mode== "a":
                showActiveAlarms()
            else:
                print "Try that again! If you need help type 'help'"
        except ValueError:
            print "Value Error"
