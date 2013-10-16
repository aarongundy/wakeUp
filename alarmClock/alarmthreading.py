# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:46:40 2013

@author: aaron
"""
import threading
import play_sound
from time import localtime
import time
import os

class AlarmClockTimer(threading.Thread):
    def __init__(self, hours, minutes,filename):
        super(AlarmClockTimer, self).__init__()

        # self.alarmData = alarmData

        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True
        self.filename = filename

    def run(self):
        # self.play_sound = play
        while self.keep_running == True:
            now = localtime()
            if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                print("ALARM NOW!")
                play_sound.playAlarmLoop("bomb_siren.wav")
                # os.popen2("aplay -q "+ self.filename)
                return
                #print "done"
            time.sleep(60)
            #print "____"
    def stop(self):
        self.keep_running = False

if __name__ == "__main__":
    alarmThread = AlarmClockTimer(20,59,"bomb_siren.wav")
    alarmThread.start()
