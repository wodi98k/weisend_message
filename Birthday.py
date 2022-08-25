import datetime
def love_day():
    in_date = '2021-5-28'
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    out_date = (datetime.datetime.now()-dt)
    new_data = out_date.days
    new_data=str(new_data)
    return new_data+"天"
def birthday():
    in_date = "-11-12"
    dt = datetime.datetime.now().strftime("%Y")
    new_date = dt+in_date
    new_data = datetime.datetime.strptime(new_date, "%Y-%m-%d")
    out_date = new_data-datetime.datetime.now()
    new_data = out_date.days
    new_data=str(new_data)
    return new_data+"天"
