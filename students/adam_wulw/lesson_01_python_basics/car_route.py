km_p_day = int(input('How meny km per day?\n'))
route = int(input('How far you are going?\n'))
extra_dey = 0;
if (route  % km_p_day  > 0):
    extra_dey = 1
print('You need at least ' + str((route  // km_p_day ) + extra_dey) + ' days')
