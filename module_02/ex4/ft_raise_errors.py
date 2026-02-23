class PlantError(Exception):
    def __init__(self) -> None:
        pass


class NameError(PlantError):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"Error: Plant name cannot be empty!"


class WaterError(PlantError):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self, level: int) -> str:
        return f"Error: Water level {level} is too high (max 10)"


class SunlightError(PlantError):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self, hour: int) -> str:
        if hour < 2:
            return f"Error: Sunlight hours {hour} is too low (min 2)"
        elif hour > 12:
            return f"Error: Sunlight hours {hour} is too high (max 12)"

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    try:
        if plant_name == "":
            raise NameError()
        else:
            print("Testing good values...")
            print(f"Plant '{plant_name}' is healthy!")
    except PlantError as error:
        print("Testing empty plant name...")
        print(error)
    print()
    try:
        if water_level < 0 or water_level > 10:
            raise WaterError()
        else:
            print("Testing good values...")
            print(f"Water level {water_level} is good")
    except PlantError as error:
        print("Testing bad water level...")
        print(error.__str__(water_level))
    print()
    try:
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise SunlightError()
        else:
            print("Testing good values...")
            print(f"Sunlight hours {sunlight_hours} is good")
    except PlantError as error:
        print("Testing bad sunlight hours...")
        print(error.__str__(sunlight_hours))


def main() -> None:
    print("=== Garden Plant Health Checker ===\n")
    plant_name = ""
    water_level = 15
    sunlight_hours = 0

    check_plant_health(plant_name, water_level, sunlight_hours)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    main()
