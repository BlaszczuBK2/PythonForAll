def policz_slowo_o_dlugosci(tekst):
    # Dzielimy tekst na słowa
    slowa = tekst.split()
    
    # Tworzymy słownik, w którym kluczem jest długość słowa, a wartością liczba wystąpień tej długości
    dlugosci = {}
    
    for slowo in slowa:
        dlugosc = len(slowo)  # Długość słowa
        if dlugosc in dlugosci:
            dlugosci[dlugosc] += 1
        else:
            dlugosci[dlugosc] = 1
            
    return dlugosci

# Wczytanie tekstu od użytkownika
tekst = input("Wprowadź tekst składający się z kilku zdań: ")

# Liczymy słowa o tej samej długości
wynik = policz_slowo_o_dlugosci(tekst)

# Wyświetlamy wynik
print("Liczba słów o tej samej długości:")
for dlugosc, liczba_slow in wynik.items():
    print(f"Długość {dlugosc}: {liczba_slow} słów")
