import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, inny_punkt):
        # Obliczanie odległości między dwoma punktami za pomocą wzoru Pitagorasa
        return math.sqrt((self.x - inny_punkt.x)**2 + (self.y - inny_punkt.y)**2)

# Przykład użycia:
punkt1 = Punkt(3, 4)
punkt2 = Punkt(7, 1)

print("Odległość między punktami:", punkt1.odleglosc(punkt2))
