import datetime
def love_day():
    in_date = '2021-5-28'
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    out_date = (datetime.datetime.now()-dt)
    new_data = out_date.days
    new_data=str(new_data)
    return new_data+"天"
def birthday():
    birth = datetime.date(2022, 11, 12)
    today = birth.today()
    if birth < today:
        new_birth = datetime.datetime(birth.year+1,month=11,day=12)
        max_day = new_birth.today()
        return str((new_birth-max_day).days)+'天'
    else:
        return str((birth-today).days)+"天"
def face_day():
    birth = datetime.date(2023, 7, 16)
    today = birth.today()
    if birth < today:
        new_birth = datetime.datetime(birth.year+1,month=1,day=17)
        max_day = new_birth.today()
        return str((new_birth-max_day).days)+'天'
    else:
        return str((birth-today).days)+"天"
