'''
Description: 
Author: zgong
Date: 2020-09-23 13:48:23
LastEditTime: 2020-09-23 13:58:30
LastEditors: zgong
FilePath: /ClassDemo/etc/run.py
Reference: 
'''
import sys
from pathlib import Path

_current_root = str(Path(__file__).resolve().parents[1])
sys.path.append(_current_root)

from utils.classTranfer import gen_class_info
from utils.Calendar import gen_calendar


def main():
    gen_class_info()
    gen_calendar()

if __name__ == "__main__":
    main()