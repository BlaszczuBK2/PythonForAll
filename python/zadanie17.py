def sortuj_wedlug_dlugosci(zdanie):
    slowa = zdanie.split()  # Podział zdania na słowa
    slowa.sort(key=len, reverse=True)  # Sortowanie według długości (malejąco)
    return " ".join(slowa)  # Łączenie listy w tekst

# Pobranie zdania od użytkownika
zdanie = input("Podaj zdanie: ")
posortowane = sortuj_wedlug_dlugosci(zdanie)

print("Posortowane słowa:", posortowane)
