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
        line = str(self.enabled)+"     "+self.name+" "*abs((12-len(self.name)))+"%2s:%2s"%(str(self.hour).zfill(2),str(self.minute).zfill(2))+"     "+self.days+"\n"
        return line