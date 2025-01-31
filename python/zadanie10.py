class Student:
    def __init__(self, imie, nazwisko, listaocen):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaocen = listaocen
        print(imie)
        print(nazwisko)
        print(listaocen)
    def srednia_ocen(self):
         liczbaocen = len(self.listaocen)
         suma = 0
         for i in range(liczbaocen):
             suma += int(self.listaocen[i])
         print(suma / liczbaocen)

if __name__ == '__main__':
    student1 = Student("Jan", "Kowalski", [3, 4, 5, 3, 5, 5, 5, 6])
    student1.srednia_ocen()

    