class Plant():
    list = []

    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self.height = self.set_height(height)
        Plant.list.append(self)

    @staticmethod
    def validate_height(height: int) -> bool:
        if height > 0:
            return True
        return False

    def set_height(self, height: int) -> int:
        if self.validate_height(height):
            return height
        return 0

    def grow(self, cm_to_grow: int) -> str:
        if cm_to_grow > 0:
            self.height += cm_to_grow
            return f"{self.name} grew {cm_to_grow}cm"
        return ""

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def blooming(self) -> str:
        if self.height > 25:
            return " (blooming)"
        return ""

    def info(self) -> str:
        return f"{super().info()}, {self.color} flowers{self.blooming()}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, point: int):
        super().__init__(name, height, color)
        self.prize = point

    def info(self) -> str:
        return f"{super().info()}, Prize points: {self.prize}"


class Garden():
    total_grow = 0

    def __init__(self, owner: str):
        self.owner = owner.capitalize()
        self.plants = []

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def grow_plants(self, cm_to_grow: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        plants_that_grew = 0
        for plant in self.plants:
            print(plant.grow(cm_to_grow))
            plants_that_grew += 1
        self.total_grow += cm_to_grow * plants_that_grew

    def sum_score(self) -> int:
        total = 0
        for plant in self.plants:
            if plant.__class__ is PrizeFlower:
                total += plant.prize
        return total


class GardenManager:
    gardens = []

    def __init__(self):
        self.stats = self.GardenStats(self)

    @classmethod
    def create_garden_network(cls, garden: Garden) -> None:
        cls.gardens.append(garden)

    class GardenStats:
        def __init__(self, manager: "GardenManager"):
            self.manager = manager

        @staticmethod
        def plants_in_garden(garden: Garden) -> None:
            for plant in garden.plants:
                print("-", plant.info())

        @staticmethod
        def info_plants(garden: Garden) -> None:
            total_plants = 0
            for plant in garden.plants:
                total_plants += 1
            total_grow = garden.total_grow
            return f"Plants added: {total_plants}, \
Total growth: {total_grow}cm"

        @staticmethod
        def plants_types(garden: Garden, plant_type) -> int:
            counter = 0
            for plant in garden.plants:
                if plant.__class__ is plant_type:
                    counter += 1
            return counter

        def info_garden(self, garden: Garden) -> None:
            print(self.info_plants(garden))
            print(f"Plant types: \
{self.plants_types(garden, Plant)} regular, \
{self.plants_types(garden, FloweringPlant)} flowering, \
{self.plants_types(garden, PrizeFlower)} prize flowers")

        @classmethod
        def validate_height(cls) -> bool:
            height_stats = True
            for garden in GardenManager.gardens:
                for plant in garden.plants:
                    if not plant.validate_height(plant.height):
                        height_stats = False
            return height_stats

        @classmethod
        def total_score(cls) -> None:
            total_garden = 0
            for garden in GardenManager.gardens:
                total_garden += 1
            i = 0
            while i < total_garden:
                garden = GardenManager.gardens[i]
                print(f"{garden.owner}: {garden.sum_score()} scores", end="")
                if i < total_garden - 1:
                    print(", ", end="")
                i += 1

        @classmethod
        def total_garden(cls) -> int:
            total = 0
            for garden in GardenManager.gardens:
                total += 1
            return total


def main() -> None:
    rose = FloweringPlant("rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)
    oak = Plant("oak tree", 100)
    pickles = Plant("pickles", 15)
    carrot = Plant("carrot", 10)
    lotus = PrizeFlower("lotus", 30, "purple", 92)

    alice = Garden("alice")
    bob = Garden("bob")
    manager = GardenManager()
    manager.create_garden_network(alice)
    manager.create_garden_network(bob)

    print("=== Garden Management System Demo ===\n")
    print(alice.add_plant(oak))
    print(alice.add_plant(rose))
    print(alice.add_plant(sunflower))
    print()
    alice.grow_plants(1)
    print()
    bob.add_plant(pickles)
    bob.add_plant(carrot)
    bob.add_plant(lotus)
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    manager.GardenStats.plants_in_garden(alice)
    print()

    manager.stats.info_garden(alice)
    print()

    print(f"Height validation test: {manager.stats.validate_height()}")
    for plant in alice.plants:
        if plant.__class__ is PrizeFlower:
            plant.prize = 218
    print("Garden scores - ", end="")
    manager.stats.total_score()
    print()
    print(f"Total gardens managed: {manager.stats.total_garden()}")


if __name__ == "__main__":
    main()
