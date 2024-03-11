import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def generate_credentials():
   # If modifying these scopes, delete the file token.json.
   SCOPES = ["https://www.googleapis.com/auth/gmail.modify"] #All read/write operations except immediate deletion of threads
  
   creds = None
   if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES) # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
         creds.refresh(Request())
      else:
         flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
         )
         creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
      with open("token.json", "w") as token:
         token.write(creds.to_json())
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
      #creds, _ = google.auth.load_credentials_from_file('credentials.json')
      
if __name__ == "__main__":
   generate_credentials()