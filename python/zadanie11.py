def znajdzSlowo(text, slowo):
    text = text.split(' ')
    numberOfWords = len(text)
    isWord = False
    for i in range(numberOfWords):
        if text[i] == slowo:
            isWord = True
            break
        
    return isWord

text = "Ala ma kota, a kot ma alę."
slowo = input("Podaj szukane słowo: ")
print(znajdzSlowo(text, slowo))