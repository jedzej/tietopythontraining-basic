def get_hours_and_minutes_on_digital_clock(all_minutes):
    hour = all_minutes // 60
    minutes = all_minutes % 60
    print('The time is {} {}'.format(hour, minutes))

if __name__ == '__main__':
    all_minutes = int(input())
    get_hours_and_minutes_on_digital_clock(all_minutes)