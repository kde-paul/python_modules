class Plant():
    list = []
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        Plant.list.append(self)
        self.bloom = False

    def bloom(self) -> None:
        if self.height > 25:
            self.bloom = True

    def grow(self, cm: int) -> str:
        self.height += cm
        self.bloom()
        return f"{self.name} grew {cm}cm"

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str, type: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.type = type

    def if_blooming(self) -> str:
        if self.bloom:
            return "(blooming)"
        return ""


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, type: str):
        super().__init__(name, height, age, color, type)
        self.prize = 0

    def set_prize(self, points) -> None:
        self.prize += points

    def get_prize(self) -> int:
        return self.prize


class Gardener():
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(Plant)
        return f"Added {plant.name} to {self.name}'s garden"


class GardenManager():
    def __init__(self):
        


def main() -> None:
    rose = FloweringPlant("rose", 25, 30, "red", "flower")
    sunflower = FloweringPlant("sunflower", 50, 45, "yellow", "flower")
    oak_tree = FloweringPlant("oak tree", 100, "", "tree")

if __name__ == "__main__":
    main()
