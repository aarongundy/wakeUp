#!/usr/bin/python

# Alarm clock

#Add function that converts weekdays to multiple days after an event

from time import localtime
import datetime
from optparse import OptionParser
import read_write
import os
# import alarmthreading
from alarmclass import *
# import alarm_gui  

def viewAlarms(alarmList):
    print ("")

    print ("Enabled\t Name\t      Time\tDays")
    print ("---------------------------------------")

    if len(alarmList)>=1:
        length = int(len(alarmList))
        #print length
        #print alarmList
        for i in range(length):
            print alarmList[i]
        print ""
    else:
        print ("The alarm array is empty")

#Find all alarms that are turned on and print them to the console
def showActiveAlarms(alarmList):
    print
    print "Enabled Alarms"
    print
    print ("Enabled\t Name\t      Time\tDays")
    print ("---------------------------------------")
    
    for alarm in alarmList:
        # print alarm
        if alarm.enabled == 'True' or alarm.enabled == True:
            print alarm

def onOff(alarmList):
    viewAlarms(alarmList)
    print
    change = raw_input("Enter the name of the alarm you would like to toggle on or off: ").strip()
    for alarm in alarmList:
        print alarm
        if alarm.name ==change:
            if alarm.enabled == True or alarm.enabled == "True":
                alarm.enabled = False
                print "You turned off alarm %s" %alarm.name
                print alarm.enabled
                break
            else:
                alarm.enabled == "True"
                print "You turned on alarm %s" %alarm.name
                break

    return alarmList

def nextAlarm(alarmList):
    today = datetime.datetime.today().weekday()
    todaysAlarms = []

    print "Today is day:",today
    #See what alarms that are in the array are happening today and are enabled
    for alarm in alarmList:
        if alarm.enabled== 'True':
            # print alarm
            if today == 0 and alarm.days== 'mon' or alarm.days== 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 1 and alarm.days== 'tues' or alarm.days== 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 2 and alarm.days== 'wed' or alarm.days== 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 3 and alarm.days== 'thurs' or alarm.days== 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 4 and alarm.days== 'fri' or alarm.days== 'wkdys':
                todaysAlarms.append(alarm)
            elif today == 5 and alarm.days== 'sat' or alarm.days== 'wknds':
                todaysAlarms.append(alarm)
            elif today == 6 and alarm.days== 'sun' or alarm.days== 'wknds':
                todaysAlarms.append(alarm)
    # print todaysAlarms
    if len(todaysAlarms)>0:
        next_alarm = todaysAlarms[0]
        for alarm in todaysAlarms:
            if not next_alarm.earlier_than(alarm):
                next_alarm = alarm
            #Start the thread that watches the time
        # alarmThread = alarmthreading.AlarmClockTimer(next_alarm[0],next_alarm[1],"bomb_siren.wav")
        # alarmThread.start()

            # if alarm[3] == 'mon' and today == 0:
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")
            # if alarm[3] == 'tues' and today == 1:
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")
            # elif alarm[3] =='wkdys' and today >= 0 and today<= 4:
            #     # print "wkdys"
            #     alarmThread = alarmthreading.Alarm(alarm[2][0],alarm[2][1],"bomb_siren.wav")

def newAlarm():
    print
    name = ""
    while name == "" or name in alarmList:
        name = raw_input("Enter the name of the alarm: ")
        if name in alarmList:
            print "Error. Can Not Be The Same Name As Another Alarm"
    new_alarm = Alarm(True,name)
    new_alarm.input_time()
    new_alarm.input_days()
    print "You created a new alarm:",(new_alarm)
    alarmList.append(new_alarm)
    print viewAlarms(alarmList)
    read_write.writeAlarmData(alarmList)
    # nextAlarm(alarmList)
    return

def printOptions():
    print "\n   Alarm Clock Options"
    print "\'q\'    \'quit\'    Quit"
    print "\'v\'    \'view\'    View Active Alarms"
    print "\'a\'    \'all\'     View All Alarms"
    print "\'t\'    \'toggle\'  Toggle Alarms on or off"

#parser = OptionParser()
#parser.add_option("-v","-viewall",help="Shows all the alarms",action="callback",callback=viewAlarms())
#(options, args) = parser.parse_args()

#________Begin Program____________
if __name__ == "__main__":
    os.system('cls' if os.name=='nt' else 'clear')

    alarmList = read_write.readAlarmData()
    alarmtime = str
    name = str
    schedule = str
    print ""

    print "*"*40
    
    print ("     Welcome to the Alarm Clock")

    print "*"*40
    
    print

    #alarmThread = alarmthreading()
    # alarmthreading.alarm.start()
    print viewAlarms(alarmList)

    print 

    run = True

    while run == True:
        time_now = localtime()
    
        print ("Current system time is: " + str(time_now.tm_hour).zfill(2) + ":" + str(time_now.tm_min).zfill(2))

        print

        nextAlarm(alarmList)
        mode = raw_input("Enter a mode: ").strip()

        mode = mode.lower()

        os.system('cls' if os.name=='nt' else 'clear') #clears the terminal

        try:
            if mode == "quit" or mode == 'q':
                # print ("Bye!")
                # raw_input()
                # alarmthreading.AlarmClockTimer("","","").stop()
                run = False
            elif mode == 'all' or mode == 'a':
                viewAlarms(alarmList)
            # elif mode == "help":
                # printOptions()
            elif mode =="t" or mode == "toggle":
                alarmList = onOff(alarmList)
                read_write.writeAlarmData(alarmList)
            elif mode == "e" or mode == "edit":
                viewAlarms(alarmList)
                alarm_name = raw_input("Enter the alarm you would like to edit: ")
                for alarm in alarmList:
                    if alarm.name ==alarm_name:
                        alarm = alarm.edit()
                        break
            elif mode == "d" or mode == "delete":
                viewAlarms(alarmList)
                alarm_name = raw_input("Enter the alarm you would like to delete: ")
                for i in range(0,len(alarmList)):
                    alarm = alarmList[i]
                    if alarm.name ==alarm_name:
                        print alarmList.pop(i)
                        break
            elif mode == "n" or mode == "new":
                newAlarm()
                read_write.writeAlarmData(alarmList)
            elif mode== "v" or mode == "view":
                showActiveAlarms(alarmList)
            elif mode== "h" or mode == "help":
                printOptions()
            else:
                print "Try that again! If you need help type 'help'"
        except ValueError:
            print "Value Error"
