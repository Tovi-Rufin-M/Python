import datetime as datetime

class ClockData:
    def __init__(self):
        self.time = self.get_time()
        self.date = self.get_date()

    def get_time(self):
        timenow = datetime.datetime.now()
        return {
            "time": timenow.strftime("%H:%M:%S"),
            "sec": timenow.strftime("%S"),
            "min": timenow.strftime("%M"),
            "hr": timenow.strftime("%H"),
        }


    def get_date(self):
        datenow = datetime.datetime.now()
        return {
            "date": datenow.strftime("%d/%m/%Y"),
            "year": datenow.strftime("%Y"),
            "month": datenow.strftime("%m"),
            "day": datenow.strftime("%d"),
        }
