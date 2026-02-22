class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(f"""=== Garden Plant Registry ===
{rose.name}: {rose.height}cm, {rose.age} days old
{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old
{cactus.name}: {cactus.height}cm, {cactus.age} days old""")
