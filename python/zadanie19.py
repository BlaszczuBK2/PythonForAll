try:
    with open("sprawdzenie.txt") as file:
        content = file.read()
        liczba_znakow = len(content)
        liczba_linii = len(content.split("\n"))
        liczba_slow = len(content.split())
        
        print("Liczba znaków w tekście: ", liczba_znakow)
        print("Liczba linii w tekście: ", liczba_linii)
        print("Liczba słów w tekście: ", liczba_slow)
except FileNotFoundError:
    print("Plik nie istnieje.")
