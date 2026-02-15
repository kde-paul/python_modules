class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    rose = Plant("Rose", 5, 3)
    sunflower = Plant("Sunflower", 15, 35)
    cactus = Plant("Cactus", 51, 53)
    print(f"""=== Garden Plant Registry ===
{rose.name}: {rose.height}cm, {rose.age} days old
{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old
{cactus.name}: {cactus.height}cm, {cactus.age} days old""")

range()