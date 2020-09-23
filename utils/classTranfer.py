'''
Description: 
Author: zgong
Date: 2020-09-20 17:36:48
LastEditTime: 2020-09-23 14:11:19
LastEditors: zgong
FilePath: /ClassDemo/utils/classTranfer.py
Reference: 
'''

import pandas as pd
import json
import re

class_info_list = []
class_week_dic = {'每周': 0, '双周': 2, '单周': 1}


def parse_class(names):
    '''
    description: #TODO 注意parse中的异常情况，必须是name(loc)(***)type的格式
    param : 
    return {type} 
    '''
    for name in names.split(';'):
        result = re.split('[()]', name)
        class_name = result[0].strip()
        class_week = class_week_dic[result[-1].strip()]
        class_loc = result[1].strip()
        yield [class_name, class_loc, class_week]


def gen_class_info():

    STARTWEEK = 1
    ENDWEEK = 16

    df = pd.read_excel('classAssignment.xls', index_col=0)
    dftime = pd.read_csv('data/classtime.csv', index_col=0)

    class_dic = {}
    for day in range(7):
        inclass = ''
        for stage in range(12):
            name = df.iloc[stage, day]
            if inclass != name:
                inclass = name
                if not pd.isna(name):
                    s = [day + 1, dftime.iloc[stage, 0], dftime.iloc[stage, 1]]
                    class_dic[name] = s
            else:
                s = class_dic[name]
                s[-1] = dftime.iloc[stage, 1]

    result = []
    for name in class_dic:
        for class_name, class_loc, class_week in parse_class(name):
            result.append([
                class_name, class_loc, class_week, *class_dic[name], STARTWEEK,
                ENDWEEK
            ])

    result = pd.DataFrame(columns=[
        'classname', 'loc', 'weekinfo', 'day', 'starttime', 'endtime',
        'startweek', 'endweek'
    ],
                          data=result)
    result.to_csv('data/class_info.csv')
