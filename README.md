Hello!

I want to use google gmail API to send cold emails because it is highly repetitive. 

What it does:
- Generate email template based on the time we have reached out
- Check current date and output the ideal date
- Create draft and send email automatically
- Record the date when creating the draft and when the email is sent
- Record the time when we should reach out again 
- Automatically update the cells in excel sheet with appropriate values 
- Coming soon: Run at least once a day in the background (schedule + nohup ... &) 

How to use it:
- pip install -m requirements.txt
- Switch working directory into Program_files
- python3 Run.py

Inputs will be taken from "Contact_tracking.xlsx". All changes will be saved here too. 
