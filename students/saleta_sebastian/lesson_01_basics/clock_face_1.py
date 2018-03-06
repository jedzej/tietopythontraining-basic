#Mam problem z odpowiednim zapisaniem tego w rownaniach, zmeczylo mnie to mam dosyc
#poprawie to jak odpoczne od tego  ;)

def calc_angle(hours, minutes, seconds):
    FULL_TURNOVER_IN_DEGREE = 360
    HOURS_IN_FULL_TURNOVER = 12
    MINUTES_IN_FULL_TURNOVER = 60
    SECONDS_IN_FULL_TURNOVER = 60

    angle = ((hours*30) + (minutes*30/60) + (seconds*30/3600))

    print(angle)

if __name__ == '__main__':
    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    calc_angle(hours, minutes, seconds)