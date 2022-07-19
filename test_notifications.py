import unittest
from unittest.mock import patch
from datetime import datetime
from datetime import timedelta
from notifications import notifications


# HELPERS #
def get_today():    # returns today's date in the format required by the program
    return str(datetime.strftime(datetime.now(), "%d.%m.%Y"))


def get_now_plus(m):    # returns current time in the format required by the program, adding m minutes
    return str(datetime.strftime(datetime.now() + timedelta(minutes=m), "%H:%M"))


# TEST #
class TestNotifications(unittest.TestCase):

    # Test for 1 correct input (current date and time + 1 minute)
    date = get_today()
    time = get_now_plus(1)

    @patch('builtins.input', side_effect=[date, time, ''])
    def test_1_input(self, mock_input):
        r = notifications()
        self.assertEqual(r['sent_notifications'], 1)
        print('')

    # Test for 2 wrong inputs
    @patch('builtins.input', side_effect=['1/08/2022', '10:00', '1 january 2023', '10 am', ''])
    def test_wrong_input(self, mock_input):
        r = notifications()
        self.assertEqual(r['sent_notifications'], 0)
        print('')

    # Test for 2 correct, 1 past and 1 wrong input
    date = get_today()
    time1 = get_now_plus(2)
    time2 = get_now_plus(3)

    @patch('builtins.input', side_effect=[date, time1, date, time2, '01.01.2001', '10:10', 'wrong_input', 'wrong_input', ''])
    def test_4_inputs(self, mock_input):
        r = notifications()
        self.assertEqual(r['sent_notifications'], 2)
        self.assertEqual(r['past_notifications'], 1)
        print('')


if __name__ == '__main__':
    unittest.main()
