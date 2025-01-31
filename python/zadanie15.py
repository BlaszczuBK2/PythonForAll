def cenzuruj(text, zakazaneSlowa):
    slowa = text.split()  # Podział na słowa (uwzględnia różne znaki)
    for i in range(len(slowa)):
        if slowa[i].strip(",.!?") in zakazaneSlowa:  # Usuwanie znaków interpunkcyjnych przed porównaniem
            slowa[i] = "***"
    tekst = " ".join(slowa)  # Poprawione "join"
    return tekst

text = "cholera, kurde, psia mać, jasna cholera!"
print(cenzuruj(text, ["cholera", "kurde", "psia",  "mać"]))
