from datetime import datetime
import time

'''
Date printer - write a script that
displays current date in human-readable format
'''

miesiace = {'01': 'styczeń', '02': 'luty', '03': 'marzec',
            '04': 'kwiecen', '05': 'maj', '06': 'czerwiec',
            '07': 'lipiec', '08': 'sierpień', '09': 'wrzesień',
            '10': 'październik', '11': 'listopad', '12': 'grudzień'}

rok = datetime.now().strftime('%Y')
miesiac = miesiace[datetime.now().strftime('%m')]
dzien = datetime.now().strftime('%d')
godzina = datetime.now().strftime('%H')
minuta = datetime.now().strftime('%M')


def todays_date():
    return 'Dzisiaj jest ' + dzien + ' ' + miesiac + ' ' + rok + ', godzina ' + godzina + ': ' + minuta


def date_from_timestamp():
    return datetime.now().fromtimestamp(time.time()).strftime('%d %b %Y %H:%M')
