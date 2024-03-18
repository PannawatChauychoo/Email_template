import datetime as dt 
from datetime import date

def suffix(d):
    #Adding suffix to date
    return {1:'st',2:'nd',3:'rd'}.get(d%20, 'th')

def convert_str(time, format_str = "%m/%d/%y %I:%M%p"):
    #Convert a time string into datetime for strftime to work
    #Could this be done in openpyxl?
    return dt.datetime.strptime(time, format_str)
   
def custom_strftime(t, format='%A %B {S} %Y at %I:%M%p'):
    #Format a string from "2/27/24 10:00pm" into "Tuesday February 27th 2024 at 10:00PM"
    if type(t) == str:
        t = convert_str(t)
    else: 
        pass
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def convert_dt(t, format_str = "%m/%d/%y %I:%M%p"):
    return t.strftime(format_str)