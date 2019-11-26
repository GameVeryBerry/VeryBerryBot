from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gspread

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1oFyoE5V38GeSM65bViTJCPgQYVnwwlmv2-bwCHhFgr0'
SAMPLE_RANGE_NAME = 'Attendance!A2:E'

def main():
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
    
    credentials = {
        'Credentials': creds.credentials
    }
    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    wks = gc.open_by_key(SAMPLE_SPREADSHEET_ID).sheet1

    wks.update_acell('B2', "it's down there somewhere, let me take another look.")

    cell_list = wks.range('A1:B7')

    # service = build('sheets', 'v4', credentials=creds)

    # # Call the Sheets API
    # sheet = service.spreadsheets()
    # # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    # #                             range=SAMPLE_RANGE_NAME).execute()
    # # values = result.get('values', [])

    # values = [
    #     [
    #         # Cell values ...
    #         "AAA",
    #         "BBB",
    #     ],
    #     # Additional rows
    # ]
    # data = [
    #     {
    #         'range': 'Attendance!A2:E',
    #         'values': values
    #     },
    #     # Additional ranges to update ...
    # ]
    # body = {
    #     'valueInputOption': 'RAW',
    #     'data': data
    # }
    # result = sheet.values().batchUpdate(
    #     spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body).execute()
    # print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[1]))

if __name__ == '__main__':
    main()