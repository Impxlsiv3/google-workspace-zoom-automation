# Google Workspace & Zoom Admin Automation

A set of Python scripts to automate Google Workspace and Zoom admin tasks using their official APIs.

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
