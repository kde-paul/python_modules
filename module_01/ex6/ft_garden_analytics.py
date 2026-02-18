class Plant():
    list = []
    def __init__(self, name: str, height: int) -> None:
        self.name = name.capitalize()
        self.height = height
        Plant.list.append(self)

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.bloom = False

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
    gardens = []
    grow_counter = 0
    score = 0
    def __init__(self, owner: str) -> None:
        self.owner = owner.capitalize()
        self.plants = []
        self.gardens.append(self)

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"
    
    def grow_plants(self) -> None:
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
            self.grow_counter += 1

    def sum_score(self) -> int:
        for plant in self.plants:
            if plant.__class__ is PrizeFlower:
                self.score += plant.prize
        return (self.score)


class GardenManager:
    gardens_list = []
    def __init__(self, garden: Garden):
        self.garden = garden
        self.gardens_list.append(self)

    def grow_garden(self, plant: Plant) -> None:
        print(self.garden.add_plant(plant))

    def help_plants(self) -> None:
        self.garden.grow_plants()
    
    class GardenStats:
        def __init__(self, manager: "GardenManager"):
            self.manager = manager

        def type_counter(self, plant_type) -> int:
            count = 0
            for plant in self.manager.garden.plants:
                if plant.__class__ is plant_type:
                    count += 1
            return count

        def plants_info(self) -> None:
            for plant in self.manager.garden.plants:
                print(plant.info())

        def garden_info(self) -> None:
            count = 0
            for plant in self.manager.garden.plants:
                count += 1
            print(f"Plants added: {count}, \
Total growth: {self.manager.garden.grow_counter}cm")
            print(f"\
Plant types: {self.type_counter(Plant)} regular, \
{self.type_counter(FloweringPlant)} flowering, \
{self.type_counter(PrizeFlower)} prize flowers")
            
        @staticmethod
        def height_validation() -> bool:
            for plant in Plant.list:
                if plant.height < 0:
                    return False
                return True

        @staticmethod
        def garden_scores() -> None:
            garden_len = 0
            for garden in Garden.gardens:
                garden_len += 1
            i = 0
            while i < garden_len:
                garden = Garden.gardens[i]
                print(f"{garden.owner}: {garden.sum_score()} scores", end="")
                if i < len(Garden.gardens) - 1:
                    print(", ", end="")
                i += 1

        def total_gardens(self) -> int:
            total = 0
            for garden in self.manager.gardens_list:
                total += 1
            return total

        def general_info(self) -> None:
            print(f"Height validation test: {self.height_validation()}")
            print("Garden scores - ", end="")
            self.garden_scores()
            print()
            print(f"Total gardens managed: {self.total_gardens()}")


def main() -> None:
    rose = FloweringPlant("rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)
    oak_tree = Plant("oak tree", 100)
    carrot = Plant("carrot", 15)
    picles = Plant("picles", 20)
    lotus = PrizeFlower("lotus", 35, "purple", 150)

    print("=== Garden Management System Demo ===\n")
    alices_garden = Garden("alice")
    alice = GardenManager(alices_garden)
    alice.grow_garden(oak_tree)
    alice.grow_garden(rose)
    alice.grow_garden(sunflower)
    print()
    alice.help_plants()
    print("""\n=== Alice's Garden Report ===
Plants in garden:""")
    alice_stats = alice.GardenStats(alice)
    alice_stats.plants_info()
    print()
    alice_stats.garden_info()
    print()
    alice_stats.general_info()

    print("=== Garden Management System Demo ===\n")
    bobs_garden = Garden("bob")
    bob = GardenManager(bobs_garden)
    bob.grow_garden(carrot)
    bob.grow_garden(picles)
    bob.grow_garden(lotus)
    print()
    bob.help_plants()
    print("""\n=== bob's Garden Report ===
Plants in garden:""")
    bob_stats = bob.GardenStats(bob)
    bob_stats.plants_info()
    print()
    bob_stats.garden_info()
    print()
    bob_stats.general_info()


if __name__ == "__main__":
    main()
