from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'
DELEGATED_ADMIN = 'admin@yourdomain.com'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(DELEGATED_ADMIN)

service = build('admin', 'directory_v1', credentials=delegated_credentials)
results = service.users().list(customer='my_customer', maxResults=10).execute()
users = results.get('users', [])

for user in users:
    print(f"{user['primaryEmail']} ({user['name']['fullName']})")
