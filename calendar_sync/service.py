import os
from datetime import datetime, timezone

from django.conf import settings
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .models import CalendarSyncState

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
CRED_PATH = os.path.join(settings.BASE_DIR, 'credentials', 'credentials.json')
TOKEN_PATH = os.path.join(settings.BASE_DIR, 'credentials', 'token.json')

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CRED_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as f:
            f.write(creds.to_json())
    return creds

def get_service():
    creds = get_credentials()
    return build('calendar', 'v3', credentials=creds)

def full_sync(calendar_id='primary'):
    svc, _ = get_service(), CalendarSyncState.objects.get_or_create(key=calendar_id)[0]
    events = svc.events().list(calendarId=calendar_id, singleEvents=True).execute()
    items = events.get('items', [])
    # TODO: Implement your business logic for saving items here
    state = CalendarSyncState.objects.get(key=calendar_id)
    state.sync_token = events.get('nextSyncToken')
    state.save()

def incremental_sync(calendar_id='primary'):
    svc = get_service()
    state, _ = CalendarSyncState.objects.get_or_create(key=calendar_id)
    if not state.sync_token:
        return full_sync(calendar_id)
    try:
        resp = svc.events().list(
            calendarId=calendar_id,
            singleEvents=True,
            syncToken=state.sync_token
        ).execute()
    except Exception:
        return full_sync(calendar_id)

    items = resp.get('items', [])
    # TODO: Implement your business logic for handling updated/deleted items here
    state.sync_token = resp.get('nextSyncToken')
    state.save()

def create_event_in_google(summary, description, start_dt, end_dt, calendar_id='primary'):
    service = get_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_dt.astimezone().isoformat(),
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': end_dt.astimezone().isoformat(),
            'timeZone': 'Europe/Moscow',
        },
    }
    return service.events().insert(calendarId=calendar_id, body=event).execute() 