class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"

class PlantError(GardenError):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Plant name cannot be empty!"


class WaterError(GardenError):
    def __init__(self, water: int) -> None:
        self.water = water

    def __str__(self) -> str:
        if self.water < 1:
            return f"Water level {self.water} is too low (min 1)"
        elif self.water > 10:
            return f"Water level {self.water} is too high (max 10)"


class SunlightError(GardenError):
    def __init__(self, sun: int) -> None:
        self.sun = sun

    def __str__(self) -> str:
        if self.sun < 1:
            return f"Sunlight hours {self.sun} is too low (min 0)"
        elif self.sun > 10:
            return f"Sunlight hours {self.sun} is too high (max 12)"


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self):
        self.plant_lst = []
        self.__water = 0
    
    def add_plant(self, name: str) -> None:
        try:
            if name == "":
                raise PlantError()
            else:
                self.plant_lst.append(Plant(name, 0, 0))
                print(f"Added {name} successfully")
        except GardenError as error:
            print("Error adding plant:", error)
    
    def water_plants(self, water: int) -> None:
        print("Opening watering system")
        try:
            for plant in self.plant_lst:
                if water < 1 or water > 10:
                    raise WaterError(water)
                else:
                    plant.water += water
                    print(f"Watering {plant.name} - success")
                    err = False
        except Exception as error:
            err = True
            print("Error watering plants:", error)
        finally:
            if err == True:
                print("Closing watering system (warning)")
            else:
                print("Closing watering system (cleanup)")
    
    def plant_health(self) -> None:
        try:
            for plant in self.plant_lst:
                if plant.sun < 2 or plant.sun > 12:
                    raise SunlightError(plant.sun)
                elif plant.water < 1 or plant.water > 10:
                    raise WaterError(plant.water)
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")
        except Exception as error:
            print(f"Error checking {plant.name}:", error)
    
    def fill_tank(self, water: int) -> None:
        try:
            if water + self.__water > 150:
                raise ValueError(f"There already are {self.__water} water in tank and more {water} water will overflow the tank")
            else:
                self.__water += water
            if self.__water < 11:
                raise GardenError("Not enough water in tank")
        except Exception as error:
            print("Caught GardenError:", error)
        finally:
            print(f"System recovered and continuing...")

def test_garden_management() -> None:
    manager = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants(5)
    print("\nChecking plant health...")
    manager.plant_lst[0].sun = 8
    manager.plant_lst[1].sun = 5
    manager.plant_lst[1].water += 10
    manager.plant_health()

    print("\nTesting error recovery...")
    manager.fill_tank(9)

    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management()
