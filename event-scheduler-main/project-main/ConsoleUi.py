import MyEventManager

api = MyEventManager.get_calendar_api()


def start_screen():
    print("Select role\n")
    print("1. Event organizer\n")
    print("2. Event attendee\n")

    user_input = int(input("Input corresponding number to select role:\t"))

    if user_input == 1:
        organizer_screen()
    elif user_input == 2:
        attendee_screen()
    else:
        print("Invalid input!\n")
        start_screen()


######### Organizer functions #########


def organizer_screen():
    # Menu
    print("Select action to perform\n")
    print("1. Create event\n")
    print("2. Update event\n")
    print("3. Delete event\n")
    print("4. Add attendee\n")
    print("5. Delete attendee\n")
    print("6. Update attendee\n")
    print("7. View attendee requests\n")
    print("8. Cancel event\n")
    print("9. Restore cancelled event\n")
    print("10. Navigate events\n")
    print("11. Search events")
    print("12. Back to role select\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        create_event_screen()

    elif user_input == 2:
        update_event_screen()

    elif user_input == 3:
        delete_event_screen()

    elif user_input == 4:
        add_attendee_screen()

    elif user_input == 5:
        delete_attendee_screen()

    elif user_input == 6:
        update_attendee_screen()

    elif user_input == 7:
        view_attendee_requests_screen()

    elif user_input == 8:
        cancel_event_screen()

    elif user_input == 9:
        restore_event_screen()

    elif user_input == 10:
        navigate_events_screen()

    elif user_input == 11:
        search_events_screen()

    elif user_input == 12:
        start_screen()

    else:
        print("Invalid input!\n")
        organizer_screen()

    # Transfer ownership

    # Delete event

    # Add attendees

    # Delete attendees

    # Update attendees

    # Check requests
    print("Organizer")


def create_event_screen():
    print("Select action to perform\n")
    print("1. Create event\n")
    print("2. Create event on behalf\n")
    print("3. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        id = str(input("Input event id:\n"))
        event_name = str(input("Input event name:\n"))
        start_time = input("Input start time (hh:mm:ss):\n")
        end_time = input("Input event end time (hh:mm:ss):\n")
        start_date = input("Input start date (YYYY-MM-DD):\n")
        end_date = input("Input event end date (YYYY-MM-DD):\n")
        event_location = str(input("Input event location:\n"))
        organizer_name = str(input("Input organizer name:\n"))
        organizer_email = str(input("Input organizer email:\n"))

        attendees_list = []

        num_attendees = int(input("Input number of attendees:\n"))

        for i in range(0, num_attendees):
            email = str(input("Input attendee email:\n"))
            name = str(input("Input attendee name:\n"))

            attendees_list.append({
                "email": email,
                "displayName": name
            })

        error_flag = False

        try:
            MyEventManager.create_event(api, id, event_name, event_location, start_time, end_time, start_date, end_date,
                                        organizer_name, organizer_email,
                                        attendees_list=[])

        except Exception as e:
            print("Failed to create event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + event_name + " successfully created")
        create_event_screen()

    elif user_input == 2:
        id = input("Input event id:\n")
        event_name = input("Input event name:\n")
        start_time = input("Input start time (hh:mm:ss):\n")
        end_time = input("Input event end time (hh:mm:ss):\n")
        start_date = input("Input start date (YYYY-MM-DD):\n")
        end_date = input("Input event end date (YYYY-MM-DD):\n")
        event_location = input("Input event location:\n")
        organizer_name = input("Input organizer name:\n")
        organizer_email = input("Input organizer email:\n")

        attendees_list = []

        num_attendees = int(input("Input number of attendees:\t"))

        for i in range(0, num_attendees):
            email = input("Input attendee email:\n")
            name = input("Input attendee name:\n")

            attendees_list.append({
                "email": email,
                "displayName": name
            })

        error_flag = False

        try:
            MyEventManager.create_event_on_behalf(api, id, event_name, event_location, start_time, end_time, start_date,
                                                  end_date,
                                                  organizer_name, organizer_email, attendees_list=[])

        except Exception as e:
            print("Failed to create event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + event_name + " successfully created")
        create_event_screen()

    elif user_input == 3:
        organizer_screen()

    else:
        print("Invalid input!\n")
        create_event_screen()


def update_event_screen():
    print("Select action to perform\n")
    print("1. Update time\n")
    print("2. Update venue\n")
    print("3. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        id = input("Input event id:\n")
        start_time = input("Input start time (hh:mm:ss):\n")
        end_time = input("Input event end time (hh:mm:ss):\n")
        start_date = input("Input start date (YYYY-MM-DD):\n")
        end_date = input("Input event end date (YYYY-MM-DD):\n")

        error_flag = False

        try:
            MyEventManager.update_event_time(api, id, start_time, end_time, start_date, end_date, True)

        except Exception as e:
            print("Failed to update event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + id + " successfully updated")
        update_event_screen()


    elif user_input == 2:
        id = input("Input event id:\n")
        venue = input("Input new venue:\n")

        error_flag = False

        try:
            MyEventManager.update_event_venue(api, id, venue, True)

        except Exception as e:
            print("Failed to update event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + id + " successfully updated")
        update_event_screen()

    elif user_input == 3:
        organizer_screen()

    else:
        print("Invalid input!\n")
        update_event_screen()


def delete_event_screen():
    print("Select action to perform\n")
    print("1. Delete event\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        id = input("Input event id:\n")

        error_flag = False

        try:
            MyEventManager.delete_event(api, id, True)

        except Exception as e:
            print("Failed to delete event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + id + " successfully deleted")

        delete_event_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        delete_event_screen()


def cancel_event_screen():
    print("Select action to perform\n")
    print("1. Cancel event\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        id = input("Input event id:\n")

        error_flag = False

        try:
            MyEventManager.cancel_event(api, id, True)

        except Exception as e:
            print("Failed to cancel event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + id + " successfully cancelled")

        cancel_event_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        cancel_event_screen()


def restore_event_screen():
    MyEventManager.display_cancelled_events()

    print("Select action to perform\n")
    print("1. Restore event\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        id = input("Input event id:\n")

        error_flag = False

        try:
            MyEventManager.restore_event(api, id, True)

        except Exception as e:
            print("Failed to restore event, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Event " + id + " successfully restored")

        restore_event_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        restore_event_screen()


def add_attendee_screen():
    print("Select action to perform\n")
    print("1. Add attendee\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        event_id = input("Input event id:\n")
        name = input("Input attendee name:\n")
        email = input("Input attendee email:\n")

        error_flag = False
        try:
            MyEventManager.add_attendee(api, event_id, name, email, True)

        except Exception as e:
            print("Failed to add attendee, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + name + " successfully added to event " + event_id)

        add_attendee_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        add_attendee_screen()


def delete_attendee_screen():
    print("Select action to perform\n")
    print("1. Delete attendee\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        event_id = input("Input event id:\n")
        email = input("Input attendee email:\n")

        error_flag = False
        try:
            MyEventManager.delete_attendee(api, event_id, email, True)

        except Exception as e:
            print("Failed to delete attendee, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + email + " successfully deleted from event " + event_id)

        delete_attendee_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        delete_attendee_screen()


def update_attendee_screen():
    print("Select action to perform\n")
    print("1. Update attendee email\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:

        event_id = input("Input event id:\n")
        old_email = input("Input attendee's current email:\n")
        new_email = input("Input attendee's new email:\n")

        error_flag = False

        try:
            MyEventManager.update_attendee(api, event_id, old_email, new_email, True)
        except Exception as e:
            print("Failed to update attendee, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + new_email + " has successfully been updated in event " + event_id)

        update_attendee_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        update_attendee_screen()


def view_attendee_requests_screen():
    MyEventManager.check_requests(True)
    print("Select action to perform\n")
    print("1. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        organizer_screen()

    else:
        print("Invalid input!\n")
        view_attendee_requests_screen()


def navigate_events_screen():
    print("Select action to perform\n")
    print("1. Navigate\n")
    print("2. Back\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        navigate_by_year_screen()

    elif user_input == 2:
        organizer_screen()

    else:
        print("Invalid input!\n")
        navigate_events_screen()

def navigate_by_year_screen(year=None):
    if year is None:
        year = input("Input starting year:\t")

    print("1. View events in " + year)
    print("2. View events in the year after " + year)
    print("3. View events in  the year before " + year)
    print("4. Back")

    second_user_input = int(input("Input corresponding number to select action:\t"))

    # 2022-09-20T10:00:33Z
    start_time = year + "-01-01T00:00:00Z"
    end_time = year + "-12-31T23:59:59Z"

    if second_user_input == 1:
        MyEventManager.filter_events(api, start_time, end_time)
        navigate_by_year_screen(year)
    elif second_user_input == 2:

        year = str(int(year) + 1)
        start_time = year + "-01-01T00:00:00Z"
        end_time = year + "-12-31T23:59:59Z"

        MyEventManager.filter_events(api, start_time, end_time)
        navigate_by_year_screen(year)
    elif second_user_input == 3:

        year = str(int(year) - 1)
        start_time = year + "-01-01T00:00:00Z"
        end_time = year + "-12-31T23:59:59Z"

        MyEventManager.filter_events(api, start_time, end_time)
        navigate_by_year_screen(year)

    elif second_user_input == 4:
        navigate_events_screen()

    else:
        print("Invalid input!\n")
        navigate_events_screen()

def search_events_screen():
    print("1. Search event")
    print("2. Back")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        event_name = input("Input event name:\t")

        MyEventManager.search_events_name(api, event_name)

    elif user_input == 2:
         organizer_screen()
    else:
        print("Invalid input!\n")
        search_events_screen()


######### Attendee functions #########

def attendee_screen():
    email = input("Input attendee email:\n")

    # Notify
    MyEventManager.notify_attendee(api, email)

    print("Select action to perform\n")
    print("1. Create event request\n")
    print("2. Respond to event invite\n")
    print("3. View events\n")
    print("4. Navigate events\n")
    print("5. Back to role select\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    # Requests
    if user_input == 1:
        attendee_request_screen(email)

    elif user_input == 2:
        attendee_respond_screen(email)

    elif user_input == 3:
        attendee_view_events_screen(email)

    elif user_input == 4:
        navigate_events_screen()

    elif user_input == 5:
        start_screen()

    else:
        print("Invalid input!\n")
        attendee_screen()


def attendee_request_screen(email):
    print("Select action to perform\n")
    print("1. Request time change\n")
    print("2. Request venue change\n")
    print("3. Back to attendee screen\n")

    user_input = int(input("Input corresponding number to select action:\t"))
    # 1. Time change
    if user_input == 1:

        event_id = input("Input event id:\n")
        start_time = input("Input new start time:\n")
        end_time = input("Input new end time:\n")

        error_flag = False
        try:
            MyEventManager.request_time_change(api, event_id, email, start_time, end_time)

        except Exception as e:
            print("Failed to create request, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + email + " has successfully made request for event " + event_id)

        attendee_request_screen(email)
    # 2. Venue change
    elif user_input == 2:
        event_id = input("Input event id:\n")
        venue_requested = input("Input new venue:\n")

        error_flag = False
        try:
            MyEventManager.request_venue_change(api, event_id, email, venue_requested)

        except Exception as e:
            print("Failed to create request, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + email + " has successfully made request for event " + event_id)

        attendee_request_screen(email)

    elif user_input == 3:
        attendee_screen()

    else:
        print("Invalid input!\n")
        attendee_request_screen(email)


def attendee_respond_screen(email):
    print("Select action to perform\n")
    print("1. Respond to invite\n")
    print("2. Back to attendee screen\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:

        response = False

        event_id = input("Input event id:\n")
        response_str = input("Are you attending the event? (Y/N):\n")

        if response_str == "Y":
            response = True
        elif response_str == "N":
            response = False
        else:
            print("Invalid input")
            attendee_respond_screen(email)

        error_flag = False
        try:
            MyEventManager.respond_to_invite(api, event_id, email, response)

        except Exception as e:
            print("Failed to respond to invite, " + str(e) + " occured")
            error_flag = True

        if not error_flag:
            print("Attendee " + email + " has successfully responded to invite for event " + event_id)

        attendee_respond_screen(email)

    elif user_input == 2:
        attendee_screen()

    else:

        print("Invalid input!\n")

        attendee_respond_screen(email)


def attendee_view_events_screen(email):
    print("Select action to perform\n")
    print("1. View events\n")
    print("2. Back to attendee screen\n")

    user_input = int(input("Input corresponding number to select action:\t"))

    if user_input == 1:
        MyEventManager.view_events(api)

    elif user_input == 2:
        attendee_screen()

    else:
        print("Invalid input!\n")

        attendee_view_events_screen(email)


# Test
if __name__ == "__main__":
    start_screen()
