try:
    with open("dane.txt") as f:
        content = f.read()
        content = content.replace(",",";")
        f.close()
    
    with open("wynik.txt", "w") as z:
        z.write(content)
        z.close()
except FileNotFoundError as e:
    print("Nie znaleziono pliku: dane.txt")