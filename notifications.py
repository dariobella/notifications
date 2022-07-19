from datetime import datetime


def notifications():
    done = False
    N = []  # list that stores all notifications to be sent
    pn = 0  # number of past notifications, for testing purposes
    sn = 0  # number of sent notifications, for testing purposes

    while not done:
        try:    # handling of input errors
            date = str(input('Please enter a date in DD.MM.YYYY format (leave blank to finish): '))
            if date != '':
                time = str(input('Please enter a time in HH:MM format: '))
                n = datetime.strptime(date + ' ' + time, "%d.%m.%Y %H:%M")  # conversion of the input in datetime format
                N.append(n)
                print('Notification saved correctly')
            else:
                done = True     # end the loop when user inputs enter
        except ValueError:  # raised when user doesn't give valid input for date conversion
            print('Input error, please check the format')

    N.sort()    # notifications are handled in chronological order

    print('\nSaved notifications: ')                        #
    for n in N:                                             # display of saved notifications
        print(datetime.strftime(n, "%d.%m.%Y - %H:%M"))     #

    print('')
    i = 1
    for n in N:
        if n < datetime.now():  # check if date is in the past
            print("The %i° notification is in the past: %s" % (i, datetime.strftime(n, "%d.%m.%Y - %H:%M")))
            pn += 1
        else:
            while not n <= datetime.now():  # wait until the time of the notification arrives
                pass
            print('%i° notification sent!' % i)
            sn += 1
        i += 1

    result = {
        'past_notifications': pn,
        'sent_notifications': sn,
        }

    return result


if __name__ == '__main__':
    r = notifications()
    print(r)
