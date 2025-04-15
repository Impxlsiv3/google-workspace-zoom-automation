# Google Workspace & Zoom Admin Automation

A set of Python automation scripts that leverage the Google Admin SDK and Zoom API to handle user provisioning, meeting scheduling, and account administration in cloud-based environments.

## Features
- List users from Google Workspace
- Create scheduled Zoom meetings
- Extendable for licensing, user provisioning, and calendar tasks

## Requirements
- Python 3
- `google-api-python-client`
- `requests`
- Zoom JWT or OAuth credentials
- Google Workspace Service Account with domain-wide delegation

## Run Example
```bash
python zoom_create_meeting.py
python gworkspace_list_users.py
```
