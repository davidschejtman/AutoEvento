import csv
import datetime
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Se você modificar os SCOPES, delete o arquivo token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def create_event(service, event_info):
    event_result = service.events().insert(calendarId='primary', body=event_info).execute()
    print(f"Evento criado: {event_result.get('summary')} ({event_result.get('id')})")
    return event_result

def read_events_from_file(file_path):
    events_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            start_dt = datetime.datetime.fromisoformat(row[0])
            end_dt = datetime.datetime.fromisoformat(row[1])
            event_info = {
                'summary': row[2],
                'description': row[3],
                'start': {'dateTime': start_dt.isoformat(), 'timeZone': 'America/Sao_Paulo'},
                'end': {'dateTime': end_dt.isoformat(), 'timeZone': 'America/Sao_Paulo'},
            }
            events_list.append(event_info)
    return events_list


def create_events_from_list(events_list):
    service = get_calendar_service()
    for event_info in events_list:
        create_event(service, event_info)

# Caminho para o arquivo de texto com os eventos
file_path = 'eventos.txt'

# Lê os eventos do arquivo e cria eles no Google Calendar
events_to_create = read_events_from_file(file_path)
create_events_from_list(events_to_create)
