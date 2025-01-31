import csv

N = int(input("Wprowadź liczbę N: "))
lista = list(range(50, 5 * N + 1))

with open("lista.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter='-')
    writer.writerow(lista)

print("Lista została zapisana do pliku lista.csv")
