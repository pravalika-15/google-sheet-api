from googleapiclient.discovery import build
from google.oauth2 import service_account


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)




# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '13nxS2w-QB-AUvD1Sanh9fFLKAFXxgwXUKxXmnUFPcco'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!A1").execute()

values = result.get('values', [])   #reading the sheet
print(result)



#writing into the sheet
value = []
row_number = 0
# input the data with spcae in between
# each value will be appended to the data in cloumn1
run = True

input_value = input("enter the data: ").split()
for i in range(len(input_value)):
    lst = []
    lst.append(input_value[i])
    value.append(lst)
    


request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sheet1", valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS", body={"values" : value})
response = request.execute()


print(response)






   