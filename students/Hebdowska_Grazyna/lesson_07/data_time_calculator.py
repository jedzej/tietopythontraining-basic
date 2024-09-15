import time


def custom_data():
    cnd = input("Give date in te format  YYYY MM DD: ")
    cnd = cnd.replace(" ", '-')
    timestamp = time.mktime(time.strptime(cnd, '%Y-%m-%d'))
    return timestamp


def count_time(t):
    new_t = t - time.time()
    s_day = 24 * 3600
    day = new_t / s_day
    print('{:.1f}'.format(day))


t = custom_data()
count_time(t)
