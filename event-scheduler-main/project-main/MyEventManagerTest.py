
import unittest
from unittest.mock import MagicMock, Mock, patch
import MyEventManager


# Add other imports here if needed

class MyEventManagerTest(unittest.TestCase):
    # This test tests number of upcoming events.
    def test_get_upcoming_events_number(self):
        num_events = 2
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        events = MyEventManager.get_upcoming_events(mock_api, time, num_events)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['maxResults'], num_events)

    # If num events < 0

    def get_event_test(self):
        pass

    
    
    
    
    # Navigation test cases:

    def test_filter_events(self):

        #test valid date, event.

        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_event2 = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'items': [mock_event],
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_api = Mock()
        mock_api.events.return_value.list.return_value.execute.return_value = mock_event2

        #test valid start date and end date
        res = MyEventManager.filter_events(mock_api, '2021-01-22T11:00:00Z', '2021-01-24T12:00:00Z')
        self.assertEqual(mock_api.events.return_value.list.return_value.execute.call_count, 1)



        #invalid start date & and end date.

        mock_event3 = {
            'id': "eventdavis12",
            'summary': "testeventdavis12",
            'location': '222 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2022-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2022-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_event4 = {
            'id': "eventdavis12",
            'summary': "testeventdavis12",
            'items': [mock_event3],
            'location': '222 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2022-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2022-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_api2 = Mock()
        mock_api2.events.return_value.list.return_value.execute.return_value = mock_event4

        #test invalid start date and end date
        res = MyEventManager.filter_events(mock_api, '2024-01-22T11:00:00Z', '2024-01-22T12:00:00Z')
        self.assertEqual(mock_api2.events.return_value.list.return_value.execute.call_count, 0)







    def test_search_events_name(self):
        mock_event = {
            'id': "eventdavis111",
            'summary': "testeventdavis111",
            'location': '223 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa1'
            },
            'start': {
                'dateTime': '2022-02-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2025-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = MagicMock(items=[mock_event])

        #test valid event name
        res = MyEventManager.search_events_name(mock_api, "testeventdavis111")
        self.assertEqual(mock_api.events.return_value.list.return_value.execute.call_count, 1)



        mock_event2 = {
            'id': "eventdavis10111",
            'summary': "testeventdavis10111",
            'location': '233 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa1'
            },
            'start': {
                'dateTime': '2022-02-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2025-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        #test invalid event name, no events
        # Test invalid address
        mock_api2 = MagicMock(items=[mock_event2])
        
        res = MyEventManager.search_events_name(mock_api2, "testeventtest")
        self.assertEqual(res, None)


    def test_view_events(self):
        # More than 0 events
        mock_event = {
            'id': "eventdavis10",
            'summary': "testeventdavis10",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2022-02-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2025-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock(items=[mock_event])

        res = MyEventManager.view_events(mock_api)
        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)


        

    def test_create_event(self):
        # Test valid id, address, start_date, end_date

        event_name = "iddfdfsdfsd"

        mock_api = Mock()

        event = MyEventManager.create_event(mock_api, "event10001", event_name, "123 Fake St. Clayton VIC 3400",
                                            "20:30:59", "21:45:55", "2022-02-04", "2022-03-04", "jastej",
                                            "jastejj@gmail.com", True, [])

        self.assertEqual(
            mock_api.events.return_value.insert.return_value.execute.return_value.get.call_count, 1)

        # Test invalid address
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                    "Clayton VIC 3400 Fake St 312",
                                                                    "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                    "jastej",
                                                                    "jastejj@gmail.com", True, [])

        # Test invalid start_date
        with self.assertRaises(IndexError):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "04/02/2020", "2022-03-04",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test invalid end_date
        with self.assertRaises(IndexError):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "2022-02-04", "04/08/2022",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test only id invalid
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, "Event_10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test not organizer
        with self.assertRaises(Exception):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                 "123 Fake St. Clayton VIC 3400",
                                                                 "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                 "jastej",
                                                                 "jastejj@gmail.com", False, [])

    def test_create_event_on_behalf(self):
        # Test valid id, address, start_date, end_date

        event_name = "iddfdfsdfsd"

        mock_api = Mock()

        event = MyEventManager.create_event(mock_api, "event10001", event_name, "123 Fake St. Clayton VIC 3400",
                                            "20:30:59", "21:45:55", "2022-02-04", "2022-03-04", "jastej",
                                            "jastejj@gmail.com", True, [])

        self.assertEqual(
            mock_api.events.return_value.insert.return_value.execute.return_value.get.call_count, 1)

        # Test invalid address
        with self.assertRaises(ValueError):

            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                    "Clayton VIC 3400 Fake St 312",
                                                                    "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                    "jastej",
                                                                    "jastejj@gmail.com", True, [])

        # Test invalid start_date
        with self.assertRaises(IndexError):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "04/02/2020", "2022-03-04",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test invalid end_date
        with self.assertRaises(IndexError):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "2022-02-04", "04/08/2022",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test only id invalid
        with self.assertRaises(ValueError):
            MyEventManager.create_event(mock_api, "Event10001", event_name,
                                                                  "123 Fake St. Clayton VIC 3400",
                                                                  "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                  "jastej",
                                                                  "jastejj@gmail.com", True, [])

        # Test not organizer
        with self.assertRaises(Exception):
            MyEventManager.create_event(mock_api, "event10001", event_name,
                                                                 "123 Fake St. Clayton VIC 3400",
                                                                 "20:30:59", "21:45:55", "2022-02-04", "2022-03-04",
                                                                 "jastej",
                                                                 "jastejj@gmail.com", False, [])

    def test_validate_id(self):
        test_id01 = "davis10101"
        self.assertTrue(MyEventManager.validate_id(test_id01))

        test_id02 = "Davis10101"
        self.assertFalse(MyEventManager.validate_id(test_id02))

        test_id03 = "jv2rs110zaowfl84c15oglnsrkt3cgmpmrxewezpxiymlw8tbfsnut4xi7f1wfkm45t05xckw5hnqaq1nruvvdhj5jpfx9r70cd43rfm4h2ocfyoubvq8919f96gbed9jnziluzf518m08p1oza5tgua72kt4lg2m5hoz6s04puvpiln7i8m98aalhb7gz8tx4mwvfkho9s5opl0wq5gqwx0yt9n5323gtoq32qnvvc0qq4574azait33j7nio7ha02kxys9mimbwsvy69pq82pzlhh3pn88in2coq77d2kvravmhe6aktt999iv5bdmzc5es1vo689eonjrjfzxlr66z474ljn4sbcqa5v1slcg0z86i5xnowpagxtj7vsyv8bh88m9qv89wshgz8b6snnp0co0fd2tc2lv68bzquv3e3yct57ox3heqko45hxf7svzmht3kunldxrmznqkh88m1gbw41ipbzysjh2fify47d6y50jxglkspzlncve3egepyxi32icq3fr03agermgxq0fm6qw49flj27s7f8xv0cb171936o5sidsa2tacx0sbtmj0rksbpzxgouce7jdu312565npbk9g8fg18chejhdh44qnldvq0c0dfqrsh297jhw4ygp0sidkm1r38zd9nin9fjyaugzpx8innoj3b4ip6hihyuaupnzog0syaky6uthqt5fky20yrs85gwe308m2nqqawqoqkwln4wm1bjsl1mnmjrr8zx2arj0wl2gxyv4a5jnmbjzgtjn0znkjrvh5w1mqffxbvc7h2s0qxf4emgfw20icetu2ag50pob97arwarg930npd7xd0z8yc7rp8gbc7wkvyc1rgrme0xj1eqo1ypwyss55buhyrzz132g4hiz2uhhmugjfypuyakcltqcn3rlc7sok5kup4tfe8dy49yh9acx7r61imhevy6ms12m7gm9qdmu3f3w8ajg79pzkmsf875f2kbvcgiqgfvwl9j8ijxse2gs7xqetlj"

        self.assertFalse(MyEventManager.validate_id(test_id03))

        test_id04 = "BEP4GPK6JLS2CJGSIMF2Y5763K9R46M806P4I68OH4VVTX1CE253F4R5PH8FEJY39G1C8DNKI4R2BVG8MYVFQXOI94R9091LO5MYYUPF1JUFNLLWVD2G0I5R6M3FG10BSUCEIMMTPSNT4STAG9J9308XC6FEU5PDG4P2RQEQENSUKX6GZWCFKB0YLXI8I5769XMX3UU25Q9GP342BOHEY7TC549AC2CS9NNI6MJU86Y3AWDPV6BDEF37ZBLPHZ7H5E7IM6PKIVU3KCRG5GJLDGV6ET1VD9ZKRSB0AB9Z2HYDSQCSJT7D7Z07YZ73LDYJH3F2T1XBGAFF8JI02HRKTWJUYU5O0LFN11ZJY5IAY7FVL0AI1H37MFELK3VRLPIMH6S0VSAQVJV8OS9X4B95XZYJKF1PT9W8GDZZQBKDAN4T66LHC1A6EEJQK19DT13DU24GORLXPW8GK93HU0WM54F1QTIOZD8HBEQUPBY0J67UKAKTMM3PEJNPI4SSTHUCP28JQHQQV147O4EKBMH0K48JKMVCJ71SE3L6RBVQ917HKBU92CCG6X73OKN82ZBHJ23R2UE4DGA4TGU7LY5BJD6O1DYAJTQVCMWHC53V1HZ1US5YN3KHLG6HPAM8NGF74RGYVCGC53SP65CG3T8IQLR6BYNJEK1BAY234VMCCLYY90ZBTZ3HRIW5GVZALOI7A8UIKTI4JAB2P5ASBNG73Q1VPJQ3DE4YYNR1ESUXOOSR9C0AJ0D1TL32TOU6PKSZJ0WG7ZE8X765F1PVN21H6GRMCOPT3WUNJ8RKE8ID12NTAX7B2TB3XN6L2W62ILRKI646PY6XFLLNI5N4K3K1EDRAIE5L85VICOK2U3O3SS6B8A9P5X7W367A601XGOUT31EPE2Q0HRTIX9HYYEHQAJBXSP2T43ZYNSFBV4W4B4NN3IM7GV3EHJ8K2BT567QMR8JOOC6L2XIVC3KY43DH5P66OXFJLDU2M4PS3YLHTPSYE9H4IAGJP6KTKT2I2AS91J0E4N"
        self.assertFalse(MyEventManager.validate_id(test_id04))

        test_id05 = "dav1"
        self.assertFalse(MyEventManager.validate_id(test_id05))

    def test_validate_date(self):
        # Valid date
        test_date01 = "12-AUG-22"
        self.assertTrue(MyEventManager.check_event_date_format(test_date01))

        # this is for first if statement false.
        test_date02 = "2022-02-22"
        self.assertTrue(MyEventManager.check_event_date_format(test_date02))

        # this is for second if statement false.
        test_date03 = "12-Aug-22"
        self.assertFalse(MyEventManager.check_event_date_format(test_date03))

        # this is for second if statement True.
        test_date04 = "2022-05-25"
        self.assertTrue(MyEventManager.check_event_date_format(test_date04))

    def test_validate_address(self):
        # path coverage

        # first case True
        test_address01 = "123 Fake Street Clayton VIC 3400"
        self.assertTrue(MyEventManager.validate_address(test_address01))

        # second case False, No house number
        test_address02 = "Fake Street Clayton VIC 3400"
        self.assertFalse(MyEventManager.validate_address(test_address02))

        # third case False, no postal code
        test_address03 = "Fake Street Clayton VIC"
        self.assertFalse(MyEventManager.validate_address(test_address03))

        # fourth case False, Malaysian address
        test_address04 = "11, Jalan 11/11, 11100, Petaling Jaya, Selangor"
        self.assertFalse(MyEventManager.validate_address(test_address04))

    # delete event test cases:

    def test_delete_event(self):
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_api = Mock()
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event
        # Organizer, event not None, event in past

        deleted_event = MyEventManager.delete_event(mock_api, "eventdavis11", True)

        self.assertEqual(mock_api.events.return_value.delete.return_value.execute.call_count, 1)

        # Organizer, event None, event in past
       
        self.assertEqual(MyEventManager.delete_event(mock_api, 'uncreatedevent',True),None)

        # Organizer, event not None, event not in past
        
        mock_event2 = {
            'id': "eventdavis111",
            'summary': "testeventdavis111",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2025-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2025-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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
        mock_api2 = Mock()
        mock_api2.events.return_value.get.return_value.execute.return_value = mock_event2

        with self.assertRaises(ValueError):
            MyEventManager.delete_event(mock_api2, 'eventdavis111', True)

        # Not organizer
        

        with self.assertRaises(Exception):
            MyEventManager.delete_event(mock_api, 'eventdavis01', False)

    # Updating event test cases
    def test_update_event_time(self):
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock()

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        # Test invalid end_date
        with self.assertRaises(IndexError):
            MyEventManager.update_event_time(mock_api, "eventid100", '12:00:00', '12:00:00',
                                                                       '2022-02-22', '23/02/2022', True)
        # Test invalid start_date
        with self.assertRaises(IndexError):
            MyEventManager.update_event_time(mock_api, "eventid100", '12:00:00', '12:00:00',
                                                                        '22/02/2022', '2022-02-23', True)
        # Test valid start_date and end_date and not None
        response = MyEventManager.update_event_time(mock_api, "eventid100", '12:00:00', '12:00:00',
                                         '2022-02-22', '2022-02-23', True)
        self.assertEqual(mock_api.events.return_value.update.return_value.execute.call_count, 1)

        # Test not organizer
        with self.assertRaises(Exception):
            MyEventManager.update_event_time(mock_api, "eventid100", '12:00:00', '12:00:00',
                                                                       '2022-02-22', '2022-02-23', False)
        # Test event None
        mock_api = Mock(event = None)
        with self.assertRaises(TypeError):
            MyEventManager.update_event_time(mock_api, "doesnotexist", '12:00:00', '12:00:00',
                                                                       '2022-02-22', '2022-02-23', True)

    def test_update_event_venue(self):
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock()

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event


        # Test invalid address
        with self.assertRaises(ValueError):

            MyEventManager.update_event_venue(mock_api, "eventid100",
                                                                       'Clayton Fake 3400 Street 123 VIC '
                                                                       , True)
        # Test valid address and not None
        MyEventManager.update_event_venue(mock_api, "eventid100",
                                         '123 Fake Street Clayton VIC 3400'
                                         ,True)
        self.assertEqual(mock_api.events.return_value.update.return_value.execute.call_count, 1)

        # Test not organizer
        with self.assertRaises(Exception):
            MyEventManager.update_event_venue(mock_api, "eventid100",
                                         '123 Fake Street Clayton VIC 3400'
                                         ,False)
        # Test event None
        mock_api = Mock(event = None)
        with self.assertRaises(TypeError):
                MyEventManager.update_event_venue(mock_api, "doesnotexist",
                                                  '123 Fake Street Clayton VIC 3400'
                                                  , True)

    def test_transfer_ownership(self):
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock()

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        # Organizer
        MyEventManager.transfer_ownership(mock_api, "eventdavis11", True, 'Jastej',
                                          'jastejj@gmail.com')
        self.assertEqual(mock_api.events.return_value.update.return_value.execute.return_value.get.call_count, 1)

        # Not organizer
        with self.assertRaises(Exception):
            MyEventManager.transfer_ownership(mock_api, "eventdavis11", False, 'Jastej',
                                                                      'jastejj@gmail.com')


    # Editing attendees as organizer test cases
    def test_add_attendee(self):
        # len attendees <= 20

        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock(event=mock_event)

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event


        MyEventManager.add_attendee(mock_api, 'eventdavis11', 'Jastej','jastejj@gmail.com', True)

        self.assertEqual(mock_api.events.return_value.update.return_value.execute.call_count, 1)

        # len attendees > 20

        more_than_20_list = [{'id':"fjhjd", 'email': "email1@gmail.com"}, {'id':"fjhjdf", 'email': "email2@gmail.com"},
                            {'id':"kjhkkj", 'email': "email3@gmail.com"}, {'id':"nmbvm", 'email': "email14@gmail.com"},
                         {'id':"khl", 'email': "email5@gmail.com"}, {'id':"dgsnbvmb", 'email': "email6@gmail.com"},
                          {'id':"fjhuyjgjjd", 'email': "email7@gmail.com"}, {'id':"fjmnnchjd", 'email': "email8@gmail.com"},
                          {'id':"fjhuijd", 'email': "email9@gmail.com"}, {'id':"cnxnvn", 'email': "email10@gmail.com"},
                          {'id':"fjdfgsfgcjhhjd", 'email': "email11@gmail.com"}, {'id':"fjnbmcbhjd", 'email': "email12@gmail.com"},
                          {'id':"fjhjhjkutkgfnd", 'email': "email13@gmail.com"}, {'id':"xvbxvcvbxxn", 'email': "email14@gmail.com"},
                          {'id':"fhlkliiyjhjd", 'email': "email15@gmail.com"}, {'id':"jhkhlk", 'email': "email16@gmail.com"},
                          {'id':"frtwerftgjhjd", 'email': "email17@gmail.com"}, {'id':"afkllszgbh", 'email': "email18@gmail.com"},
                          {'id':"fjhjjlhfhfbnukld", 'email': "email19@gmail.com"}, {'id':"vkgkute", 'email': "email20@gmail.com"}]

        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': more_than_20_list,
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
        mock_api = Mock(event=mock_event)
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event
        with self.assertRaises(Exception):
            MyEventManager.add_attendee(mock_api, 'eventdavis11', 'Jastej','jastejj@gmail.com', True)

        # not organizer
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = Mock(event=mock_event)
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event
        with self.assertRaises(Exception):
            MyEventManager.add_attendee(mock_api, 'eventdavis11', 'Jastej', 'jastejj@gmail.com', False)

    def test_delete_attendee(self):
        # Len_attendees > 1 email not found
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [{'email': 'jastejj@gmail.com'}],
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

        mock_api = MagicMock()

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        # Len_attendees > 1 and email not found
        with self.assertRaises(ValueError):
            MyEventManager.delete_attendee(mock_api, "eventdavis11", "doesntexist@gmail.com", True)

        # Len_attendees > 1 email found
        MyEventManager.delete_attendee(mock_api, "eventdavis11", "jastejj@gmail.com", True)
        self.assertEqual(mock_api.events.return_value.update.return_value.execute.call_count, 1)

        # Len_attendees < 1
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        # Len_attendees == 0
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        with self.assertRaises(Exception):
            MyEventManager.delete_attendee(mock_api, "eventdavis11", "jastejj@gmail.com", True)

        # Not organizer
        with self.assertRaises(Exception):
            MyEventManager.delete_attendee(mock_api, "eventdavis11", "jastejj@gmail.com", False)

    # # Editing attendees as organizer test cases

    def test_update_attendee(self):
    #     # Len_attendees > 0 email not found
        mock_event = {
            'id': "eventdavis30",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [{'email': 'jastejj@gmail.com'}],
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

        mock_api = MagicMock()

        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        with self.assertRaises(ValueError):
            MyEventManager.update_attendee(mock_api, "eventdavis30", "jastejjjjjjjj@gmail.com", "jastejj@gmail.com", True)


    #     # Len_attendees > 0 email found
        self.assertEqual(MyEventManager.update_attendee(mock_api, "eventdavis30", "jastejj@gmail.com", "davishwa5@gmail.com", True), True)

            
    #     # Len_attendees = 0
        mock_event2 = {
            'id': "eventdavis311",
            'summary': "testeventdavis311",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api2 = MagicMock()

        mock_api2.events.return_value.get.return_value.execute.return_value = mock_event2
        with self.assertRaises(Exception):
            MyEventManager.update_attendee(mock_api2, "eventdavis311", "jastejjjjjjjj@gmail.com", "jastejj@gmail.com", True)

        # Not organizer
        with self.assertRaises(Exception):
            MyEventManager.update_attendee(mock_api, "eventdavis30", "jastejj@gmail.com", "davishwa5@gmail.com", False)

     
      
    def test_notify_attendee(self):

        # Len_attendees > 0 email not found (invalid email test)
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'dhwa0003@student.monash.edu',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [{"email": "jastejj@gmail.com"}, {"email": "davishwa5@gmail.com"}],
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

        
        mock_event2 = {
                'id': "eventdavis10",
                'summary': "testeventdavis10",
                'location': '123 Fake Street Clayton VIC 3400',
                "organizer": {
                    "email": 'dhwa0003@student.monash.edu',
                    "displayName": 'davishwa'
                },
                'start': {
                    'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
                },
                'end': {
                    'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
                },
                'attendees': [{"email": "jastejj@gmail.com"}, {"email": "davishwa5@gmail.com"}],
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

        
        mock_calendar = {
            "kind": "calendar#events",
            "items": [
                mock_event, mock_event2
            ]
            }
        mock_api = MagicMock()
        mock_api.events.return_value.list.return_value.execute.return_value = mock_calendar
        with self.assertRaises(ValueError):
            MyEventManager.notify_attendee(mock_api,'jjjjjj@gmail.com')


    #     # Len_attendees > 0 email found

        mock_api2 = MagicMock()
        mock_api2.events.return_value.list.return_value.execute.return_value = mock_calendar
        
        self.assertTrue(MyEventManager.notify_attendee(mock_api2,"jastejj@gmail.com"))
            

    #     # Len_attendees = 0
        mock_event3 = {
                'id': "eventdavis101",
                'summary': "testeventdavis101",
                'location': '123 Fake Street Clayton VIC 3400',
                "organizer": {
                    "email": 'dhwa0003@student.monash.edu',
                    "displayName": 'davishwa'
                },
                'start': {
                    'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
                },
                'end': {
                    'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
                },
                'attendees': [],
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


        mock_calendar2 = {
            "kind": "calendar#events",
            "items": [
                mock_event3
            ]
        }

        mock_api3 = MagicMock()
        mock_api3.events.return_value.list.return_value.execute.return_value = mock_calendar2
        
        with self.assertRaises(ValueError):
            MyEventManager.notify_attendee(mock_api3,"davishwa5@gmail.com")

        def test_respond_to_invite(self):
            mock_event = {
                'id': "eventdavis11",
                'summary': "testeventdavis11",
                'location': '123 Fake Street Clayton VIC 3400',
                "organizer": {
                    "email": 'davishwa5@gmail.com',
                    "displayName": 'davishwa'
                },
                'start': {
                    'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
                },
                'end': {
                    'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
                },
                'attendees': [{'email': 'davishwa5@gmail.com', 'responseStatus': "needsAction"}],
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

            mock_api = MagicMock()
            mock_api.events.return_value.get.return_value.execute.return_value = mock_event

            # Len_attendees > 0 email not found
            with self.assertRaises(ValueError):
                MyEventManager.respond_to_invite(mock_api, "eventdavis11", "doesntexist@gmail.com", True)

            # Len_attendees > 0 email found, accept invite
            response = MyEventManager.respond_to_invite(mock_api, "eventdavis11", "davishwa5@gmail.com", True)

            self.assertEqual(mock_api.events.return_value.get.return_value.execute.call_count, 2)

            # Len_attendees > 0 email found, reject invite
            response = MyEventManager.respond_to_invite(mock_api, "eventdavis11", "davishwa5@gmail.com", False)

            self.assertEqual(mock_api.events.return_value.get.return_value.execute.call_count, 4)

            # Len_attendees < 0
            mock_event = {
                'id': "eventdavis11",
                'summary': "testeventdavis11",
                'location': '123 Fake Street Clayton VIC 3400',
                "organizer": {
                    "email": 'davishwa5@gmail.com',
                    "displayName": 'davishwa'
                },
                'start': {
                    'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
                },
                'end': {
                    'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
                },
                'attendees': [],
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

            mock_api = MagicMock()
            mock_api.events.return_value.get.return_value.execute.return_value = mock_event

            with self.assertRaises(ValueError):
                MyEventManager.respond_to_invite(mock_api, "eventdavis11", "doesntexist@gmail.com", True)

    def test_request_time_change(self):
        mock_requests = []

        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [{'email': 'davishwa5@gmail.com', 'responseStatus': "needsAction"}],
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


        mock_api = MagicMock()
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        # request_time_change(api, event_id, email, start_time_requested, end_time_requested)

        # Len_attendees > 0, Invalid start_time
        with self.assertRaises(IndexError):
            MyEventManager.request_time_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "22/08/2022", "2022-08-28", mock_requests)

        #  Len_attendees > 0, Invalid end time
        with self.assertRaises(IndexError):
            MyEventManager.request_time_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "2022-08-22",
                                               "28/08/2022", mock_requests)
        # Len_attendees > 0, email found,
        response = MyEventManager.request_time_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "2022-08-22",
                                               "2022-08-26", mock_requests)

        self.assertEqual(len(mock_requests), 1)

        # Len_attendees > 0, email not found
        with self.assertRaises(ValueError):
            MyEventManager.request_time_change(mock_api, "eventdavis11", 'nonexistent@gmail.com', "2022-08-22",
                                                      "2022-08-26", mock_requests)

        # Len_attendees < 0
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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


        with self.assertRaises(ValueError):
            MyEventManager.request_time_change(mock_api, "eventdavis11", 'nonexistent@gmail.com', "2022-08-22",
                                                      "2022-08-26", mock_requests)


    def test_request_venue_change(self):
        mock_requests = []

        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [{'email': 'davishwa5@gmail.com', 'responseStatus': "needsAction"}],
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

        mock_api = MagicMock()
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        # request_venue_change(api, event_id, email, venue_requested)
        # Len_attendees > 0 Invalid address
        with self.assertRaises(ValueError):
            MyEventManager.request_venue_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "Clayton VIC 3400 Fake St 312", mock_requests)

        # Len_attendees > 0 email found,
        response = MyEventManager.request_venue_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "123 Fake Street Clayton VIC 3400",  mock_requests)

        self.assertEqual(len(mock_requests), 1)

        # Len_attendees > 0 email not found
        with self.assertRaises(ValueError):
            MyEventManager.request_venue_change(mock_api, "eventdavis11", 'nonexistent@gmail.com', "123 Fake Street Clayton VIC 3400", mock_requests)

        # Len_attendees < 0
        mock_event = {
            'id': "eventdavis11",
            'summary': "testeventdavis11",
            'location': '123 Fake Street Clayton VIC 3400',
            "organizer": {
                "email": 'davishwa5@gmail.com',
                "displayName": 'davishwa'
            },
            'start': {
                'dateTime': '2021-01-22' + 'T' + '12:00:00' + 'Z'
            },
            'end': {
                'dateTime': '2021-01-23' + 'T' + '12:00:00' + 'Z'
            },
            'attendees': [],
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

        mock_api = MagicMock()
        mock_api.events.return_value.get.return_value.execute.return_value = mock_event

        with self.assertRaises(Exception):
            MyEventManager.request_venue_change(mock_api, "eventdavis11", 'davishwa5@gmail.com', "123 Fake Street Clayton VIC 3400",  mock_requests)




def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(MyEventManagerTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)

    # num_events = 2
    # time = "2020-08-03T00:00:00.000000Z"

    # mock_api = Mock()
    # events = MyEventManager.get_upcoming_events(mock_api, time, num_events)

    # args, kwargs = mock_api.events.return_value.list.call_args_list[0]
    # # self.assertEqual(kwargs['maxResults'], num_events)
    # print(args)


main()
