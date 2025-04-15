from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'credentials.json'
DELEGATED_ADMIN = 'admin@yourdomain.com'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(DELEGATED_ADMIN)

service = build('admin', 'directory_v1', credentials=delegated_credentials)

user_body = {
    "name": {"givenName": "Jane", "familyName": "Doe"},
    "password": "TempPass1234",
    "primaryEmail": "janedoe@yourdomain.com"
}

result = service.users().insert(body=user_body).execute()
print(f"Created user: {result['primaryEmail']}")
