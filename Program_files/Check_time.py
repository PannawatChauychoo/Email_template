import datetime as dt 
import random
import time

#Tuesday -> Thursday from 8-10am are go time
def check_ideal_sendtime(prefer_weekdays = [1,2,3], prefer_hours = [8,9,10]):
    """
    Finding the ideal time to send based on current time
    """
    now = dt.datetime.now() #example: datetime.datetime(2024, 3, 6, 20, 56, 59, 727333)
    go_days = prefer_weekdays
    go_hours = [8,9,10]

    year = now.year
    weekday = now.weekday() #int (0-6) -> 0 = Monday, 6 = Sunday
    hour = now.hour 
    date = now.day
    month = now.month

    random_hour = random.randint(8,10)
    random_minute = random.randint(0, 59)

    today_date_str = now.strftime("%A") #weekday str
    
    if weekday in go_days:
        print("yes")
        if hour in go_hours:
            print(f"Today is {today_date_str} and in prime_time! Let's send them!")
            scheduled_time = now
        elif hour not in go_hours and weekday < max(go_days):
            print(f"Today is {today_date_str} but not in primetime! Let's send them tomorrow!")
            scheduled_time = dt.datetime(year, month, date + 1, random_hour, random_minute)
        elif hour not in go_hours and weekday >= max(go_days):
            wait_time = 6 - weekday + min(go_days) # Count the days to next Tuesday
            scheduled_time = dt.datetime(year, month, date + wait_time, random_hour, random_minute)
            scheduled_day = scheduled_time.strftime("%A")
            print(f"Today is {today_date_str} but we missed the ideal time. Let's schedule emails for next week on {scheduled_day}")        
    elif weekday > max(go_days):
        print("Too late")
        wait_time = 6 - weekday + min(go_days) # Count the days to next Tuesday
        scheduled_time = dt.datetime(year, month, date + wait_time, random_hour, random_minute)
        scheduled_day = scheduled_time.strftime("%A")
        print(f"Today is {today_date_str}. Let's schedule emails for next week on {scheduled_day}")
    elif weekday < min(go_days):
        print("Too early")
        scheduled_time = dt.datetime(year, month, date + 1, random_hour, random_minute) #Since it is Monday then schedule on Tuesday
        print(f"Today is {today_date_str}. Let's schedule emails for tomorrow!")
    else: 
        pass
    
    return scheduled_time