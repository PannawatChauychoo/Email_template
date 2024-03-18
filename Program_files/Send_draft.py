# [START gmail_send_message]
import base64
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import argparse

def gmail_send_draft(draft_id, recipient):
  """Create and insert a draft email.
   Print the returned draft's message and id.
   Returns: Draft object, including draft id and message meta data.
  """
  creds = Credentials.from_authorized_user_file("token.json")

  try:
    # create gmail api client
    service = build("gmail", "v1", credentials= creds)
    
    # pylint: disable=E1101
    send_draft = (
        service.users()
        .drafts()
        .send(userId="me", body={"id": draft_id})
        .execute()
    )
    #print(f'Draft with ID {draft_id} sent successfully to {recipient}.')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_draft = None
  return send_draft

  

def check_if_sent(message_id):
  message = (
    service.users()
    .messages()
    .get(userId='me', id=message_id)
    .execute()
    )

  # Check if the "SENT" label is present in the message's labelIds
  if 'SENT' in message.get('labelIds', []):
    send_status = 1
  else:
    send_status = 0
  
  return send_status


def main():
  # defined command line options/this also generates --help and error handling
  CLI = argparse.ArgumentParser(description="Craft email draft based input")
  
  CLI.add_argument(
  "draft_id",  # name on the CLI - drop the `--` for positional/required parameters
  type=str,
  )
  CLI.add_argument(
  "recipient",  # name on the CLI - drop the `--` for positional/required parameters
  type=str,
  )
  
  # parse the command line
  args = CLI.parse_args()
  # access CLI options
  gmail_send_draft(args.draft, args.recipient)

if __name__ == "__main__":
  main()