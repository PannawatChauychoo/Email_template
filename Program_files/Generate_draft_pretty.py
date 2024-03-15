#Automatically compost emails based on the excel sheet with the drafts 


import argparse
import base64
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials


def create_htmldraft(body_message, recipient):
   """Create and insert a draft email with html formatting
      Print the returned draft's message and id.
      Returns: Draft object, including draft id and message meta data.
   """
   creds = Credentials.from_authorized_user_file("token.json")

   try:
      # create gmail api client
      service = build("gmail", "v1", credentials= creds)
      
      #Trying to send html text
      #Start
      message = EmailMessage()
      content = body_message
      
      #message = MIMEText(body_message, 'html')
      message["To"] = str(recipient)
      message["Subject"] = "USC senior looking for advice"
      
      message.add_header('Content-Type', 'text/html')
      message.set_content(content, subtype= 'html')
      #End

      # encoded message
      encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

      create_message = {"message": {"raw": encoded_message}}
      # pylint: disable=E1101
      draft = (
         service.users()
         .drafts()
         .create(userId="me", body=create_message)
         .execute()
      )

      print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

   except HttpError as error:
      print(f"An error occurred: {error}")
      draft = None
   return draft

def main():
      # defined command line options/this also generates --help and error handling
   CLI = argparse.ArgumentParser(description="Craft email draft based input")
      
   CLI.add_argument(
      "draft",  # name on the CLI - drop the `--` for positional/required parameters
      type=str,
      )
      
   CLI.add_argument(
   "recipient",  # name on the CLI - drop the `--` for positional/required parameters
   type=str,
   )
      
      # parse the command line
   args = CLI.parse_args()
   # access CLI options
   create_htmldraft(args.draft, args.recipient)

if __name__ == "__main__":
   main()
