# Date printer - script that displays current date in human-readable format
import datetime

now = datetime.datetime.now()

print('Full current date and time using str method of datetime object: ', str(now))
print(str(now.day) + '.' + str(now.month) + '.' + str(now.year))
print(str(now.day) + '.' + str(now.month) + '.' + str(now.year)
      + ' ' + str(now.hour) + ':' + str(now.minute))


print("\nCurrent date and time using instance attributes:")
print('Year: %d' % now.year)
print('Month: %d' % now.month)
print('Day: %d' % now.day)
print('Hour: %d' % now.hour)
print('Minute: %d' % now.minute)
print('Second: %d' % now.second)
print('Microsecond: %d' % now.microsecond)

print("\nCurrent date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M"))
print(now.strftime("%d.%m.%Y %H:%M"))
print(now.strftime("%d %B %Y %H:%M"))   # month by word

print("\nCurrent date and time using isoformat:")
print(now.isoformat())
