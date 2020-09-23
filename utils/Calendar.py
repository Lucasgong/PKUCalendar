'''
Description: 
Author: zgong
Date: 2020-09-20 20:35:02
LastEditTime: 2020-09-23 14:05:46
LastEditors: zgong
FilePath: /ClassDemo/utils/Calendar.py
Reference: 
'''
import datetime
from ics import Calendar, Event, DisplayAlarm
import pandas as pd

ALARM = """BEGIN:VALARM
TRIGGER:-PT20M
REPEAT:1
DURATION:PT5M
ACTION:DISPLAY
DESCRIPTION:class begin
END:VALARM
END:VEVENT"""

TIMEZONE = datetime.timedelta(hours=-8)


class PKUCalendar():
    def __init__(self):
        self.c = Calendar()
        # self.alarm = DisplayAlarm(trigger=[datetime.timedelta(minutes=20)],
        #                           display_text='class begin')

    def add_event(self, class_name, begin, end):
        e = Event()
        e.name = class_name
        e.begin = begin
        e.end = end
        self.c.events.add(e)

    def save(self, name):
        name = 'my.ics'
        with open(name, 'w') as handler:
            handler.writelines(self.c)

        # set replacement string

        with open(name, 'r+') as handler:
            # read current calender
            data = handler.read()
            # jump to first line again
            handler.seek(0)
            # write new calender
            handler.write(data.replace('END:VEVENT', ALARM))


def gen_calendar():
    pkucal = PKUCalendar()

    first_week = input("请设置第一周的星期一日期(如：20200921):")
    first_week = datetime.datetime.strptime(first_week, '%Y%m%d')
    dfclass = pd.read_csv('data/class_info.csv', index_col=0)

    for idx, row in dfclass.iterrows():
        # 具体日期计算出来
        className = row["classname"] + '@' + row["loc"]

        endtime = row["endtime"]
        endtime = datetime.timedelta(hours=int(endtime[:2]),
                                     minutes=int(endtime[3:]))
        starttime = row["starttime"]
        starttime = datetime.timedelta(hours=int(starttime[:2]),
                                       minutes=int(starttime[3:]))

        startWeek = row['startweek']
        endWeek = row['endweek']
        weekday = row['day']

        weekinfo = row['weekinfo']  #0:每周，1:单周，2:双周
        during = [7, 14, 14][weekinfo]
        if weekinfo == 2:
            startWeek = [startWeek + 1, startWeek][startWeek // 2]

        dateLength = float((int(startWeek) - 1) * 7)
        startDate = first_week + datetime.timedelta(days=dateLength + weekday -
                                                    1)

        dateLength = float((int(endWeek) - 1) * 7)
        endDate = first_week + datetime.timedelta(days=dateLength + weekday -
                                                  1)

        today = startDate
        while True:
            begin = (today + starttime +
                     TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
            end = (today + endtime + TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
            pkucal.add_event(className, begin, end)
            today = today + datetime.timedelta(days=during)
            if (today > endDate):
                break
    pkucal.save('pku.ics')

