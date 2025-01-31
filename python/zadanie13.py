class Pracownik:
    def __init__(self, imie, nazwisko, stawka_godzinowa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka_godzinowa = stawka_godzinowa

    def oblicz_wynagrodzenie(self, liczba_godzin):
        return self.stawka_godzinowa*liczba_godzin
    
if __name__ == '__main__':
    pracownik1 = Pracownik("Kamil", "Błaszczyk", 1000)
    print(pracownik1.oblicz_wynagrodzenie(40))
