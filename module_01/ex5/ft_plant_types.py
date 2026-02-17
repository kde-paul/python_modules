class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, \
{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.t_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, \
{self.age} days, {self.t_diameter}cm diameter")

    def produce_shade(self, shade: int) -> None:
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        print(f"{self.name} (Vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest")

    def nutritional_value(self, vitamin: str) -> None:
        print(f"{self.name} is rich in vitamin {vitamin.capitalize()}")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 25, 30, "red")
    rose.bloom()
    print()
    oak = Tree("oak", 500, 1825, 50)
    oak.produce_shade(78)
    print()
    tomato = Vegetable("tomato", 80, 90, "summer")
    tomato.nutritional_value("C")
    print()

    print("=== Garden Plant Types ===")
    sunflower = Flower("sunflower", 80, 45, "yellow")
    sunflower.bloom()
    print()
    methuselah = Tree("methuselah", 1000, 2455, 100)
    methuselah.produce_shade(123)
    print()
    carrot = Vegetable("carrot", 15, 45, "spring")
    carrot.nutritional_value("A")


if __name__ == "__main__":
    main()
