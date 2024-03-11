import pandas as pd 
from datetime import datetime as dt 
from datetime import date

from Generate_templates import write_email
from Generate_draft import gmail_create_draft
from Check_creds import generate_credentials
from Check_time import check_ideal_sendtime

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

"""
Goal of functionality:
- Generate email template based on the time we have reached out
- Check current date and output the ideal date
- Create draft and send email automatically
- Record the date when creating the draft and when the email is sent
- Record the time when we should reach out again 
- Automatically update the cells with appropriate values 
- Bonus: Run at least once a day in the background (schedule + nohup ... &) - https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

"""


def row_into_string(row_list):
    #Combining all values of a row into a string
    output_string = ", ".join([str(i) for i in row_list])
    return output_string

def suffix(d):
    #Adding suffix to date
    return {1:'st',2:'nd',3:'rd'}.get(d%20, 'th')

def convert_str(time, format_str = "%m/%d/%y %I:%M%p"):
    #Convert a time string into datetime for strftime to work
    return dt.strptime(time, format_str)
   
def custom_strftime(t, format='%A %B {S} %Y at %I:%M%p'):
    #Format a string from "2/27/24 10:00pm" into "Tuesday February 27th 2024 at 10:00PM"
    if type(t) == str:
        t = convert_str(t)
    else: 
        pass
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def main():
    #Getting user credentials
    generate_credentials()
    
    target = pd.read_excel('../Data/Contact_tracking.xlsx', sheet_name= "Targets")
    my_info = pd.read_excel('../Data/Contact_tracking.xlsx', sheet_name= "Myself")
    
    #Combining my info into a my info strings + availabilities
    my_email = my_info.iloc[0, 0]
    my_info_strings = my_info.iloc[0, 1:6].apply(row_into_string, axis = 1)
    avail = my_info.iloc[0, 6:]
    my_formatted_info = my_info_strings + ", " + ", ".join([custom_strftime(avail[i][0]) for i in avail]) #Getting the right format for dates

    #Combining all rows into strings
    target_input_strings = target.iloc[:, 1:7].apply(row_into_string, axis = 1) 
    
    #Check for the right scheduled time for this batch
    ideal_time = check_ideal_sendtime()
    
    #Create a draft for every email
    for i in range(0, len(target)):
        email = target.iloc[i, 0]
        follow_up_count = target.iloc[i, 6]
        response = target.iloc[i, 7]
        
        excel_row = i + 2
        
        
        #Check if they have responded
        if response.lower() == 'yes':
            print('Awesome! Goodluck with the informational interview.')
        elif responded.lower() == 'no' and follow_up_count < 3:
            try:
                #generate template
                email_draft_template = write_email(target_input_strings[i], my_formatted_info[0])
                gmail_create_draft(email_draft_template, email[i], my_email)
                print(f"Draft for {email} created!")
        
            except ValueError:
                print("Something went wrong...")
            

    
    #Update excel files 
    

if __name__ == "__main__":
    main()