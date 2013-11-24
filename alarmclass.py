class Alarm(object):
    """docstring for  date"""
    def __init__(self, enabled = False,name="No Name",hour=0, minute = 0,days = None):
        # super( date, self).__init__()
        self.enabled = enabled
        self.name = name
        self.hour = hour
        self.minute = minute
        self.days = days

    def __str__(self):
        line = ''
        if self.enabled == True or self.enabled =="True":
            line = str(self.enabled)+"     "+self.name+" "*abs((12-len(self.name)))+"%2s:%2s"%(str(self.hour).zfill(2),str(self.minute).zfill(2))+"        "+self.days+"\n"
        else:
            line = str(self.enabled)+"    "+self.name+" "*abs((12-len(self.name)))+"%2s:%2s"%(str(self.hour).zfill(2),str(self.minute).zfill(2))+"        "+self.days+"\n"

        return line

    def earlier_than(self,other):
        if self.hour<other.hour:
            return True
        elif self.hour == other.hour and self.minute<other.minute:
            return True
        else:
            return False

    def edit(self):
        print
        print self

        edit_mode = raw_input("Enter what you would like to edit(time,days,name):")

        edit_mode = edit_mode.lower()
        if edit_mode == "time":
            self.input_time()
        elif edit_mode == "days":
            self.input_days
        elif edit_mode == "name":
            self.input_name()
        return self

    def input_time(self):
        while True:
            alarmtime = raw_input("Enter the time: ")
            alarmtime = alarmtime.split(":")
            alarmtime[0] = int(alarmtime[0])
            alarmtime[1] = int(alarmtime[1])
            if alarmtime[0]>= 0 and alarmtime[0]<=23 and alarmtime[1]>=0 and alarmtime[1]<=59:
                self.hour = alarmtime[0]
                self.minute = alarmtime[1]
                break
            else:
                print "**Please enter a valid time in 24 hour format**"

    def input_days(self):
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
        self.days = schedule

    def input_name(self):
        self.name = raw_input("Enter a name:")