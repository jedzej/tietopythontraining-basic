hours = int(input())
minutes = int(input())
seconds = int(input())

hour_div = 12
min_div = hour_div * 60
sec_div = min_div * 60

print((hours / hour_div + minutes / min_div + seconds / sec_div) * 360)
