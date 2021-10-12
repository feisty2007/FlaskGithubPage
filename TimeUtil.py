import time


class TimeUtil:
    def __init__(self) -> None:
        pass

    def today(self):
        t = time.localtime(time.time())

        return "%s-%s-%s" % (t.tm_year,t.tm_mon,t.tm_mday)

    def now(self):
        t = time.localtime(time.time())

        return TimeObj(t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)

    def getTime(self):
        return time.localtime(time.time())


class TimeObj:
    def __init__(self,year,month,day,hour,minute,second) -> None:
        self.year = year
        self.month = month
        self.day = day

        self.hour = hour
        self.minute = minute
        self.second = second

    def toStr(self):
        return "%s-%s-%s %s:%s:%s" % (self.year,self.month,self.day,self.hour,self.minute,self.second)

    def __str__(self) -> str:
        return self.toStr()