class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


def main() -> None:
    plant_lst = {
        "plant_1": {"name": "Rose", "height": 25, "age": 30},
        "plant_2": {"name": "Oak", "height": 200, "age": 365},
        "plant_3": {"name": "Cactus", "height": 5, "age": 90},
        "plant_4": {"name": "Sunflower", "height": 80, "age": 45},
        "plant_5": {"name": "Fern", "height": 15, "age": 120},
    }
    counter = 0
    for x in plant_lst:
        name = plant_lst[x]["name"]
        height = plant_lst[x]["height"]
        age = plant_lst[x]["age"]
        plant_lst[x] = Plant(name, height, age)
        counter += 1
    print(f"\nTotal plants created: {counter}")


if __name__ == "__main__":
    main()
