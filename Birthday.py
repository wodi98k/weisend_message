import datetime
from hashlib import new
def love_day():
    in_date = '2021-5-28'
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    out_date = (datetime.datetime.now()-dt)
    new_data = out_date.days
    new_data=str(new_data)
    return new_data+"天"