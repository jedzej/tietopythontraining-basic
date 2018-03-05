print ('Podaj liczbę')
a = int(input())
liczba_setek = a//100
a = a - liczba_setek*100
liczba_dziesiatek = a//10
a = a - liczba_dziesiatek*10
liczba_jendnosci = a//1
print ('Suma cyfr w liczie wynosi',liczba_dziesiatek+liczba_setek+liczba_jendnosci)