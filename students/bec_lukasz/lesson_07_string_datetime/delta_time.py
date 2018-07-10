from datetime import datetime

'''
Delta time calculator - write a script that
calculates time difference in days between
current date and custom date in the future.
'''

current_date_string = datetime.now().strftime('%d-%m-%Y')


def time_delta(date):
    user_date = datetime.strptime(date, '%d-%m-%Y')
    actual_date = datetime.strptime(current_date_string, '%d-%m-%Y')
    return (user_date - actual_date).days


print(time_delta('23-05-2019'))
