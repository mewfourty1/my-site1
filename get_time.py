from  datetime import datetime,timedelta
def get_base():
    now = datetime.now()
    now_min=now.minute
    now_h = now.hour
    amount = timedelta(hours=1)
    amount_1=timedelta(days=1)
    if now_min <=40 and now_h==0:

        ans=now - amount_1
        base_date=ans.strftime("%Y%m%d")
        base_time=ans.strftime("%H00")
    elif now_min <=40:

        ans1=now-amount
        base_date = ans1.strftime("%Y%m%d")
        base_time = ans1.strftime("%H00")
    else:

        base_date = now.strftime("%Y%m%d")
        base_time = now.strftime("%H00")
    return base_date,base_time
if __name__ == "__main__":
    print(get_base())