import datetime

def brithday_work():
    today = datetime.date.today()
    year = int(str(today)[0:4])
    month = int(str(today)[5:7])
    month_day = int(str(today)[8:10])
    month_31 = [1, 3, 5, 7, 8, 10, 12]

    def year_opinion():
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            year_ping()
        else:
            return year_run()

    def year_ping():
        print(year_run() + 1)

    def year_run():
        day = 12
        sum = month + 1  
        if month in month_31:
            day += 31-month_day
            while sum <= 10:
                if sum == 12:
                    day += 31
                    sum == 1
                elif sum in month_31:
                    day += 31
                    sum += 1
                else:
                    if sum == 2:
                        day += 28
                        sum += 1
                    else:
                        day += 30
                        sum += 1
        else:
            day += 30 - month_day  
        return str(day)+"天"

    return year_opinion()
