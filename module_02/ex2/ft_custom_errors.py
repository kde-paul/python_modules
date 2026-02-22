class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__
        self.message = message

    def message(self) -> str:
        return f"Caught a garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def message(self) -> str:
        return f"Caught PlantError: {self.message}"

class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)
    
    def message(self) -> str:
        return f"Caught WaterError: {self.message}"
    

def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_wilting = True
        if plant_wilting:
            raise PlantError("The tomato plant is wilting!")
    except PlantError:
        print(PlantError.message)
    try:
        print("Testing WaterError...")
        tank_full = False
        if not tank_full:
            raise WaterError("WaterError")
    except WaterError:
        print(WaterError("Not enough water in the tank!").message)


if __name__ == "__main__":
    main()