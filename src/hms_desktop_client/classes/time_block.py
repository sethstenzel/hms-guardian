import time

class TimeBlock:
    hour_map =  {
        "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12,
        "13":13, "14":14, "15":15, "16":16, "17":17, "18":18, "19":19, "20":20, "21":21, "22":22, "23":23
    }
    quarter_map = {
        "a":15,
        "b":30,
        "c":45,
        "d":0
    }
    @classmethod
    def allowed(time_blocks:list):
        for time_block in time_blocks:
            current_time = time.localtime()
            hour, quarter = tuple(time_block.split('.'))
            if current_time.tm_hour == hour and current_time.tm_min <= TimeBlock.quarter_map[quarter]:
                return True
        return False