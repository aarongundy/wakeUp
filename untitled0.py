# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:36:20 2013

@author: aaron
"""
alarm = []
i =0

f = open("alarmdata")

while 1:
    line = f.readline().strip()

    if not line: break    
    
    alarm[i].append((line.split("|",4))
    print "", alarm[i]
    
    i=i+1
    
    

f.close()