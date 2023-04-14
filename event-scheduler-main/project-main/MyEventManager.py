

# Code adapted from https://developers.google.com/calendar/quickstart/python
from __future__ import print_function
from ast import Delete
import datetime
from importlib import invalidate_caches
from logging import captureWarnings
import pickle
import os.path
from queue import Empty

import pytz as pytz
import utc as utc
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import usaddress
# pip install python-dateutil
from dateutil.relativedelta import relativedelta
from dateutil import parser
# For checking http error
import urllib.request
import urllib.error

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Global variable of cancelled events
cancelled_events = []

# For datetime
utc = pytz.UTC


def get_calendar_api():
    """
    Get an object which allows you to consume the Google Calendar API.
    You do not need to worry about what this function exactly does, nor create test cases for it.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def get_event(api, calendar_id, event_id):
    event = api.events().get(calendarId=calendar_id, eventId=event_id).execute()

    if event != {}:
        return event
    else:
        return None


def get_upcoming_events(api, starting_time, number_of_events):
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next n events on the user's calendar.
    """
    if (number_of_events <= 0):
        raise ValueError("Number of events must be at least 1.")

    events_result = api.events().list(calendarId='primary', timeMin=starting_time,
                                      maxResults=number_of_events, singleEvents=True,
                                      orderBy='startTime').execute()
    return events_result.get('items', [])


# validate date format strategy refer from stackedoverflow "https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python"

def check_event_date_format(date):
    """
    returns true for yyyy-mm-dd (2022-02-22) format or dd-MON-yy (12-AUG-22)
    strftime() will act to validate paddings
    """

    # if date format is alphabetical abbreviation: 
    if date.split("-")[1] in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:

        # preprocessing, taking MON out of date and changing to Mon then joining.
        temp = date.split("-")
        capitalised_month = date.split("-")[1].capitalize()  # "Aug"
        temp[1] = capitalised_month
        date = '-'.join(temp)

        # validation part, if false, means wrong format.
        try:
            if datetime.datetime.strptime(date, "%d-%b-%y").strftime('%d-%b-%y'):
                return True
        except ValueError:
            return False

    # else, if date format is (2022-02-22) or
    else:
        # print(date)
        # try:
        #     if (datetime.datetime.strptime(date, "%d-%b-%y").strftime('%d-%b-%y')):
        #         return True

        # except ValueError:

        try:
            if (datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d')):
                return True

        except ValueError:
            return False


# check time format


# With the help of usaaddress https://usaddress.readthedocs.io/en/latest/
def validate_address(address):
    dict_list = usaddress.parse(address)
    address_dict_format = dict((x, y) for y, x in dict_list)

    control_keys = ['AddressNumber', 'StreetName', 'StreetNamePostType', 'PlaceName', 'StateName', 'ZipCode']
    control_keys.sort()
    live_keys = list(dict.keys(address_dict_format))
    live_keys.sort()

    if live_keys == control_keys:
        return True
    else:
        return False


def validate_id(event_id):
    if (len(event_id) >= 5 and len(event_id) <= 1024) and event_id.islower():
        return True
    else:
        return False

######### Event organiser ############

# Create event
# add sendUpdates attribute for notification.
# reminders added for 24 hours in advance.
# Date time object: 2022-09-24T14:31:41.702404Z
#  id has to be between 5 and 1024, No uppercase
def create_event(api, id, event_name, event_location, start_time, end_time, start_date, end_date, organizer_name,
                 organizer_email, organizer: bool,
                 attendees_list=[]
                 ):
    if organizer:
        if validate_address(event_location) and check_event_date_format(start_date) and check_event_date_format(
                end_date):
            start_date_time = start_date + "T" + start_time + 'Z'
            end_date_time = end_date + "T" + end_time + 'Z'

            if not validate_id(id):
                raise ValueError("Invalid Id, Id must be more than 5 characters and less than 1024 characters")

            else:
                event_body = {
                    'id': id,
                    'summary': event_name,
                    'location': event_location,
                    "organizer": {
                        "email": organizer_email,
                        "displayName": organizer_name
                    },
                    'start': {
                        'dateTime': start_date_time
                    },
                    'end': {
                        'dateTime': end_date_time
                    },
                    'attendees': attendees_list,
                    'maxAttendees': 20,
                    "guestsCanInviteOthers": 'False',
                    "sendUpdates": "all",  # update of event creation
                    "reminders": {
                        "useDefault": False,
                        # Overrides can be set if and only if useDefault is false.
                        "overrides": [
                            {"method": 'email', 'minutes': 24 * 60},  # reminder by email only (one day in advance)
                        ]
                    }
                }

                event = api.events().insert(calendarId='primary', body=event_body).execute()
                return event.get('summary')
                print('Event created: %s' % (event.get('htmlLink')))

        else:
            raise ValueError("Times and/or address provided not valid")
    else:
        raise Exception("Only organizer can update events!")


# Update events
def update_event_time(api, id, start_time, end_time, start_date, end_date, organizer: bool):
    if organizer:
        event = get_event(api, 'primary', id)

        # If exists, delete
        if event is not None:
            if check_event_date_format(start_date) and check_event_date_format(end_date):
                start_date_time = start_date + "T" + start_time + 'Z'
                end_date_time = end_date + "T" + end_time + 'Z'

                event['start']['dateTime'] = start_date_time
                event['end']['dateTime'] = end_date_time

                event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
                return event

            else:
                raise ValueError("Times provided not valid")

        else:
            # Else, raise exception
            raise ValueError("Event does not exist")

    else:
        raise Exception("Only organizer can update events!")


# Update events
def update_event_venue(api, id, venue, organizer: bool):
    if organizer:
        event = get_event(api, 'primary', id)

        # If exists, delete
        if event is not None:
            if validate_address(venue):
                event['location'] = venue

                event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
                return event

            else:
                raise ValueError("Venue address provided not valid")

        else:
            # Else, raise exception
            raise ValueError("Event does not exist")

    else:
        raise Exception("Only organizer can update events!")


# Delete
# Method to delete events
def delete_event(api, _eventId, organizer: bool):
    if organizer:
        current_time = datetime.datetime.utcnow()

        event = get_event(api, 'primary', _eventId)

        # If exists, delete
        if event is not None:
            if parser.parse(event['end'].get('dateTime')) < utc.localize(current_time):
                api.events().delete(calendarId='primary', eventId=_eventId).execute()
                return print("Event has been deleted")

            else:
                raise ValueError("Event is not from the past")

        else:
            # Else, raise exception
            raise ValueError("Event does not exist")

    else:
        raise Exception("Only organizer can delete events!")


def cancelled_events_duplicate_check(event_id):
    for event in cancelled_events:
        if event['id'] == event_id:
            return True
    return False


def cancel_event(api, event_id, organizer: bool, cancelled_events=cancelled_events):
    if organizer:
        if validate_id(event_id):
            event = get_event(api, 'primary', event_id)

            if event is not None:
                for event in cancelled_events:

                    duplicate = cancelled_events_duplicate_check(event_id)

                    if event['id'] == event_id and not duplicate:
                        cancelled_events.append(event)
                    else:
                        raise ValueError("Event already cancelled")
        else:
            raise ValueError("Invalid event id")
    else:
        raise Exception("Only organizer can cancel events!")
    return cancelled_events


def display_cancelled_events():
    print("Cancelled events:")

    for event in cancelled_events:
        print(event['id'])


def restore_event(api, event_id, organizer: bool, cancelled_events = cancelled_events):
    if organizer:
        display_cancelled_events()

        event = get_event(api, 'primary', event_id)

        duplicate = cancelled_events_duplicate_check(event_id)

        if event is not None and duplicate:
            cancelled_events.remove(event)

        else:
            raise ValueError("Event has not been cancelled")
    else:
        raise Exception("Only organizer can cancel events!")


# Create event on behalf
def create_event_on_behalf(api, id, event_name, event_location, start_time, end_time, start_date, end_date,
                           organizer_name, organizer_email, organizer: bool,
                           attendees_list=[]):
    if organizer:

        if validate_address(event_location) and check_event_date_format(start_date) and check_event_date_format(
                end_date):
            start_date_time = start_date + "T" + start_time + 'Z'
            end_date_time = end_date + "T" + end_time + 'Z'

            if not validate_id(id):
                raise ValueError("Invalid Id, Id must be more than 5 characters and less than 1024 characters")
            else:
                event_body = {
                    'id': id,
                    'summary': event_name,
                    'location': event_location,
                    "organizer": {
                        "email": organizer_email,
                        "displayName": organizer_name
                    },
                    'start': {
                        'dateTime': start_date_time
                    },
                    'end': {
                        'dateTime': end_date_time
                    },
                    'attendees': attendees_list,
                    'maxAttendees': 20,
                    "guestsCanInviteOthers": 'False',
                    "sendUpdates": "all",  # update of event creation
                    "reminders": {
                        "useDefault": False,
                        # Overrides can be set if and only if useDefault is false.
                        "overrides": [
                            {"method": 'email', 'minutes': 24 * 60},  # reminder by email only (one day in advance)
                            # {"method": 'popup', 'minutes': 10},
                        ]
                    }
                }

                event = api.events().insert(calendarId='primary', body=event_body).execute()
                print('Event created: %s' % (event.get('htmlLink')))
        else:
            raise ValueError("Invalid time or address")

    else:
        raise Exception("Only organizer can cancel events!")


def transfer_ownership(api, event_id, organizer: bool, new_organizer_name, new_organizer_email):
    if organizer:

        # First retrieve the event from the API.
        event = api.events().get(calendarId='primary', eventId=event_id).execute()

        event['organizer']['email'] = new_organizer_email
        event['organizer']['displayName'] = new_organizer_name

        updated_event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

        # Print the updated date.
        return updated_event.get('updated')


    else:
        raise Exception("Only organizer can transfer ownership")


# Add attendees
def add_attendee(api, event_id, name, email, organizer: bool):
    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    if organizer:
        if len(event['attendees']) < 20:

            event['attendees'].append({
                "email": email,
                "displayName": name
            })

            updated_event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
            print(updated_event.get('updated'))
        else:
            raise Exception("Guest list full!")

    else:
        raise Exception("Only organizer can add guests!")


# Delete attendees
def delete_attendee(api, event_id, email, organizer: bool):
    found_flag = False

    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    if organizer:
        attendees = event.get('attendees')
        if len(attendees) > 0:

            print(attendees)

            for attendee in attendees:
                print(attendee)
                if email in attendee['email']:
                    attendees.remove(attendee)
                    found_flag = True
                    print("Email found")

                if found_flag:
                    updated_event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
                    print(updated_event.get('updated'))

                else:
                    raise ValueError("Attendee not found")

        else:
            raise Exception("Guest list empty!")

    else:
        raise Exception("Only organizer can delete guests!")


# Update attendees
def update_attendee(api, event_id, old_email, new_email, organizer: bool):
    found_flag = False

    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    if organizer:
        if len(event['attendees']) > 0:
            attendees = list(event['attendees'])
            print(attendees)

            for attendee in attendees:
                print(attendee)

                if old_email in attendee.get('email'):
                    attendee['email'] = new_email
                    return True

                    found_flag = True

            if found_flag:
                updated_event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
                print(updated_event['updated'])

            elif not found_flag:
                raise ValueError("Attendee not found")

        else:
            raise Exception("Guest list empty!")

    else:
        raise Exception("Only organizer can update guests!")


######### Attendees ############

# Notify
def notify_attendee(api, attendee_email):
    found_flag = False

    events_response = api.events().list(calendarId='primary', q=attendee_email).execute()
    events = events_response['items']
    for event in events:
        if len(event['attendees']) > 0:
            attendees = list(event['attendees'])
            print(attendees)

            for attendee in attendees:
                if attendee_email in attendee.get('email'):
                    found_flag = True
                    print("You are an attendee for event " + event.get('summary'))
                    return True

    for event in cancelled_events:
        if len(event['attendees']) > 0:
            attendees = list(event['attendees'])
            print(attendees)

            for attendee in attendees:
                if attendee_email in attendee.get('email'):
                    print(event['summary'] + " has been cancelled")

                    found_flag = True

    if not found_flag:
        raise ValueError("Attendee not found")


# Accept/Reject invite
# True: Accept invite 
# False: Reject invite

def respond_to_invite(api, event_id, email, response: bool):
    found_flag = False

    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    if len(event['attendees']) > 0:
        attendees = event['attendees']

        for attendee in attendees:
            if attendee.get('email') == email:

                # If accept
                if response:
                    attendee['responseStatus'] = "accepted"

                # If reject
                elif not response:
                    attendee['responseStatus'] = "declined"

                    delete_attendee(api, event['id'], email, True)

                found_flag = True

        if found_flag:
            updated_event = api.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
            print(updated_event['updated'])

        else:
            raise ValueError("Attendee not found")
    else:
        raise ValueError("Guest list empty")


attendee_requests = []


# Request change of time
def request_time_change(api, event_id, email, start_time_requested, end_time_requested,
                        attendee_requests=attendee_requests):
    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    found_flag = False

    if check_event_date_format(start_time_requested) and check_event_date_format(end_time_requested):

        if len(event['attendees']) > 0:
            attendees = event['attendees']

            for attendee in attendees:
                if attendee.get('email') == email:
                    found_flag = True

            if found_flag:
                attendee_requests.append(
                    "Attendee " + email + " has requested start time change " + str(
                        start_time_requested) + " and end time change " + str(end_time_requested) + " for event " +
                    event['summary'] +
                    " with id " + event_id
                )
            elif not found_flag:
                raise ValueError("Attendee not found")

        else:
            raise ValueError("Attendees list empty!")

    else:
        raise ValueError("Invalid time")


# Request change of venue
def request_venue_change(api, event_id, email, venue_requested, attendee_requests=attendee_requests):
    event = api.events().get(calendarId='primary', eventId=event_id).execute()

    found_flag = False

    if validate_address(venue_requested):

        if len(event['attendees']) > 0:
            attendees = event['attendees']

            for attendee in attendees:
                if attendee.get('email') == email:
                    found_flag = True

            if found_flag:
                attendee_requests.append(
                    "Attendee " + email + " has requested venue change " + str(venue_requested) + " for event " + event[
                        'summary'] +
                    " with id " + event_id
                )

            elif not found_flag:
                raise ValueError("Attendee not found")

        else:
            raise Exception("Attendees list empty!")

    else:
        raise ValueError("Invalid address")


# Display requests
def check_requests(organizer: bool):
    if organizer:

        if len(attendee_requests) > 0:
            for request in attendee_requests:
                print(request + "\n")

        else:
            print("No requests")
    else:
        raise Exception("Only organizer can check requests!")


# View events (+/- 5 years)
def view_events(api):
    current_date = datetime.datetime.now().isoformat() + 'Z'

    year = int(current_date[0: 4])

    time_min = str(year - 5) + current_date[4:]

    time_max = str(year + 5) + current_date[4:]

    counter = 0

    page_token = None

    events = api.events().list(calendarId='primary', pageToken=page_token, timeMin=time_min,
                               timeMax=time_max).execute()

    return events.get('items', [])


# view events based on start date and end date (organizer only)  : all events and reminders will be displayed.
def filter_events(api, start_time, end_time):
    date = start_time.split("T")[0]
    end_date = end_time.split("T")[0]
    if not check_event_date_format(date) and check_event_date_format(end_date):
        raise ValueError("Invalid date format")

    else:

        counter = 0

        page_token = None
        while True:
            events = api.events().list(calendarId='primary', pageToken=page_token, timeMin=start_time,
                                       timeMax=end_time).execute()
            for event in events['items']:
                temp = counter + 1
                print("Event number: " + str(temp))
                print(event.get('summary'))
                print(event.get('reminders'))
                counter += 1

            page_token = events.get('nextPageToken')
            if not page_token:
                break

        return counter


def search_events_name(api, event_name):
    event = api.events().list(calendarId='primary', q=event_name, singleEvents=True).execute()
    if event['items'] == []:
        raise ValueError("No event with this ID!")
    else:
        print(event['items'])


def main():
    api = get_calendar_api()
    time_now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    # events = get_upcoming_events(api, time_now, 10)

    # print(time_now)

if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()
