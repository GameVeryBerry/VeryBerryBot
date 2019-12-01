import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# pip install pygsheets
import pygsheets

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1oFyoE5V38GeSM65bViTJCPgQYVnwwlmv2-bwCHhFgr0'


def get_credentials():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('credentials/token.pickle'):
        with open('credentials/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/spreadsheet.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('credentials/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def get_index(l, x, default=False):
    return l.index(x) if x in l else default


def main():
    creds = get_credentials()
    gc = pygsheets.authorize(custom_credentials=creds)
    wks = gc.open_by_key(SPREADSHEET_ID).sheet1
    #Access all of the record inside that
    ids = wks.get_col(1)
    row = get_index(ids, '9', None)
    if not row == None:
        data = wks.get_row(row + 1)
        print(data)

if __name__ == '__main__':
    main()
