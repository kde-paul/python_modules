def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is not None:
                print(f"Watering {plant}")
            else:
                raise ValueError
    except Exception as error:
        print(f"Error: Cannot water {error.__cause__} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_lst = ["tomato", "lettuce", "carrots"]
    wrong_lst = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_lst)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(wrong_lst)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
