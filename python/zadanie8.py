zdanie = input("Podaj przykładowe zdanie: ")
list = zdanie.split(" ")

print(list[len(list)-1], end=" ")
for i in range(1, len(list)-1):
    print(list[i], end=" ")
print(list[0], end=" ")