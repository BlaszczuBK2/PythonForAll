class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return 3.14 * self.promien ** 2
    
if __name__ == '__main__':
    k1 = Kolo(5)
    pole1 = k1.oblicz_pole()
    print(f"Pole koła o promieniu 5 wynosi: {pole1:.2f}")