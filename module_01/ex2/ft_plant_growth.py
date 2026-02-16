class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1

    def get_info(self, day) -> None:
        self.day = day
        print(f"""=== Day {self.day} ===
{self.name}: {self.height}cm, {self.days} days old""")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    rose.get_info(1)
    for growth in range(6):
        rose.grow()
        rose.age()
        growth += 1
    rose.get_info(7)
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
