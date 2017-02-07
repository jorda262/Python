#This program creates various instances of different classes for
#presenting information in the form of standard dates, standard
#times, military time, and standard date and time together. Each class
#has a constructor(__init__), a setter, a getter, and some have fucntions
#that convert or show (print) something
def main():
    print("Standard time:")
    time1 = Time(8,36,0,'PM')
    print( time1.getTime() )
    time1.showTime();
    print()

    print("Standard date:")
    date1 = Date(13,10,2015)
    print( date1.getDate())
    date1.showDate()
    print()

    print("Date time: ")
    dt1 = DateTime(8,36,0,'PM',13,10,2015)
    print(dt1.getDateTime())
    dt1.showDateTime()
    print()

    print("Military time:")
    mt1 = MilitaryTime(2236,22)
    print(mt1.getMilitaryTime())
    mt1.showMilitaryTime()
    mt1.showStandardTime()
    
#Class for standard time being displayed in a standard format     
class Time:

    def __init__(self, hour=0, minute=0, second=0, period = 'AM'):
        self.setTime(hour, minute, second, period)

    def getTime(self):
        return self.vars
    
    def setTime(self, hour, minute, second, period):
        self.vars = (hour, minute, second, period)

    def showTime(self):
        print("{}:{}:{} {}".format(self.vars[0], self.vars[1], self.vars[2], self.vars[3]))

#Class for military time.
class MilitaryTime(Time):

    def __init__(self, militaryHours=0, militarySeconds=0):
        self.setMilitaryTime(militaryHours, militarySeconds)

    def getMilitaryTime(self):
        return self.military
    
    def setMilitaryTime(self, militaryHours=0, militarySeconds=0):
        self.military = (militaryHours, militarySeconds)

    def showMilitaryTime(self):
        print("{}:{} hours".format(self.military[0], self.military[1]))

    def convertToStandard(self):
        self.hour = int(str(self.military[0])[:2])%12
        self.minute = str(self.military[0])[-2:]
        self.second = self.military[1]
        if (int(str(self.military[0])[:2])/12) > 1:
            self.period = 'PM'
        else:
            self.period = 'AM'

        self.standard = Time(self.hour, self.minute, self.second, self.period)        

    def showStandardTime(self):
        self.convertToStandard()
        self.standard.showTime()

#Class for displaying the standard date in the form month day, year        
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.setDate(day, month, year)

    def getDate(self):
        return self.date
    
    def setDate(self, day, month, year):
        self.date = (day, month, year)

    def showDate(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
        print("{} {}, {}".format(months[self.date[1]], self.date[0], self.date[2]))

#Class for displaying the standard time and the standard date
class DateTime(Date, Time):

    def __init__(self, *args):
        self.var = args
        self.time = Time(self.var[0], self.var[1], self.var[2], self.var[3])
        self.date = Date(self.var[4], self.var[5], self.var[6])
        
    def getDateTime(self):
        return self.var[0:3] + self.var[-3:]
    
    def setDateTime(self, hour, minute, second, period, day, month, year ):
        self.time = Time(hour, minute, second, period)
        self.date = Date(day, month, year)

    def showDateTime(self):
        self.time.showTime()
        self.date.showDate()
    
if __name__ == "__main__": main()
