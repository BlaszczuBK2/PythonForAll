l = ["zielony", "niebieski", "zółty", "czerwony", "pomarańczowy"]
j = input("Podaj kolor: ")
for i in range(0,4):
    if l[i] == j:
        print(f"Znaleziono kolor {j} na pozycji {i+1}")
        break
    else:
        print(f"Nie znaleziono koloru {j}")