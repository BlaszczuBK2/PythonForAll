my_dict = {'Kamil': 30, 'Brygida': 21}
oldest_name = ''
oldest_age = 0

for name, age in my_dict.items():
    if age > oldest_age:
        oldest_name = name
        oldest_age = age

print(f"The oldest person is {oldest_name} with age {oldest_age}.")
