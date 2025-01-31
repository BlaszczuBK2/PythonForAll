class Bilet:
    def __init__(self, miejsca, rzad, cena):
        self.miejsca = miejsca
        self.rzad = rzad
        self.cena = cena

    def pokazBilet(self):  # Dodano 'self'
        print("Miejsce: ", self.miejsca)  # Poprawiono 'self.miejsc' na 'self.miejsca'
        print("Rząd: ", self.rzad)
        print("Cena: ", self.cena)
    
class BiletVip(Bilet):
    def __init__(self, miejsca, rzad, cena, strefa_vip):
        super().__init__(miejsca, rzad, cena)  # Użyto super() zamiast Bilet.__init__()
        self.strefa_vip = strefa_vip

    def pokazBilet(self):  # Przysłonięcie metody w klasie Bilet
        super().pokazBilet()  # Wywołanie metody klasy bazowej
        print("Strefa VIP: ", self.strefa_vip)
