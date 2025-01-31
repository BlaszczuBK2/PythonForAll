class Zwierze:
    def dajGlos(self):
        print("Dźwięk zwierzęcia")

class Pies(Zwierze):
    def dajGlos(self):  # Poprawiona nazwa metody
        print("Hau hau")

class Kot(Zwierze):
    def dajGlos(self):  # Poprawiona nazwa metody
        print("Miau")

if __name__ == "__main__":
    pies = Pies()
    pies.dajGlos()  # Teraz poprawnie wypisze: Hau hau

    kot = Kot()
    kot.dajGlos()   # Teraz poprawnie wypisze: Miau
