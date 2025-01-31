import random
import json

class MyClass:
    def __init__(self, name: str = None, value: int = None):
        self.name = name if name else f"Item{random.randint(1, 100)}"
        self.value = value if value else random.randint(1, 1000)
    
    def to_dict(self):
        return {"name": self.name, "value": self.value}


def generate_objects(count: int):
    return [MyClass() for _ in range(count)]


def save_objects_to_file(objects, filename="objects.json"):
    with open(filename, "w") as file:
        json.dump([obj.to_dict() for obj in objects], file, indent=4)


# Przykład użycia
objects_list = generate_objects(10)
save_objects_to_file(objects_list)
