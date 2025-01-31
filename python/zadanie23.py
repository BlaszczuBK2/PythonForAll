class Komparator:
    def __init__(self, tekst_1, tekst_2):
        self.tekst_1 = tekst_1
        self.tekst_2 = tekst_2
        self.wynik = None  # Inicjalizacja wyniku jako None

    def porownaj(self):
        # Porównanie tekstów i zapisanie wyniku
        if self.tekst_1 == self.tekst_2:
            self.wynik = f"{self.tekst_1} jest identyczny jak {self.tekst_2}"
        else:
            self.wynik = f"{self.tekst_1} jest różny od {self.tekst_2}"

    def podaj_wynik(self):
        # Wyświetlenie wyniku porównania
        if self.wynik:
            print(self.wynik)
        else:
            print("Porównanie nie zostało jeszcze wykonane.")

# Przykład użycia:
tekst1 = input("Wprowadź pierwszy tekst: ")
tekst2 = input("Wprowadź drugi tekst: ")

komparator = Komparator(tekst1, tekst2)
komparator.porownaj()
komparator.podaj_wynik()
