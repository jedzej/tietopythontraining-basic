daily_distance = int(input())
route = int(input())
if route % daily_distance:
    # jeżeli na przejechanie dystansu potrzeba choćby godzinę kolejnego dnia,
    # trzeba doliczyć odatkowy dzień. Modulo czli % zwraca resztę z dzielenia.
    # Jeżeli na przejechanie dysntansu potrzeba np. dwa i pół dnia, to pół dnia
    # traktujemy jako resztę. Resztę musimy dodać jako kolejny cały dzień,
    #  dlatego w princie jest +1
    print(route // daily_distance + 1)
else:
    print(route // daily_distance)
    # w przeciwnym wypadku - jeśli całość trasy uda nam się zmieścić w pełnych
    #  dniach, bez rozpoczynania kolejnego, a więc bez reszty - nie dodajemy
    #  niczego i drukujemy tylko liczbę wykorzystanych dni.
