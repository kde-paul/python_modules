class GardenError(Exception):
    def __init__(self) -> None:
        pass


class PlantError(GardenError):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "The tomato plant is wilting!"


class WaterError(GardenError):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "Not enough water in the tank!"


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_wilting = True
        if plant_wilting:
            raise PlantError()
    except PlantError as error:
        print("Caught PlantError:", error)
    print()
    try:
        print("Testing WaterError...")
        tank_full = False
        if not tank_full:
            raise WaterError()
    except WaterError as error:
        print("Caught WaterError:", error)
    print()
    try:
        print("Testing catching all garden errors...")
        garden_error = True
        if garden_error:
            raise PlantError()
    except GardenError as error:
        print("Caught WaterError:", error)
    try:
        garden_error = True
        if garden_error:
            raise WaterError()
    except GardenError as error:
        print("Caught WaterError:", error)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
