import datetime
import struct
import time

from backtrader.feed import DataBase
from backtrader import date2num
from backtrader import TimeFrame
import backtrader as bt

import numpy as np
import pandas as pd
import requests
import json

class AlgoLiveData(DataBase):
    def __init__(self,endpoint):
        super(AlgoLiveData, self).__init__()
        self.endpoint=endpoint

    def start(self):
        print("start feed")

    def stop(self):
        print("stop feed")

    def _load(self):
        now=datetime.datetime.now()
        print("load feed")
        try:
            print("[%s]:poll data:%s" % (now,self.endpoint))
            r = requests.get(url = self.endpoint, timeout=5) 
            print("status=%s,res=%s" % (r.status_code,r.text))
            if r.status_code == 200:
                data=json.loads(r.text)
                dt=pd.to_datetime(data.date, format = "%Y-%m-%d")
                close=data.close
                self.lines.datetime[0] = date2num(dt)
                self.lines.open[0] = close
                self.lines.high[0] = close
                self.lines.low[0] = close
                self.lines.close[0] = close
                self.lines.volume[0] = 0
                print("poll data successful")
                time.sleep(1)
            else:
                time.sleep(5)
        except:
            print("could not poll data")
            time.sleep(5)
        return True