def check_temperature(temp_str: str) -> None:
    try:
        temp_int = int(temp_str)
        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        elif temp_int > 45:
            print(f"Error: {temp_int} is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    i = 0
    while i < 4:
        temperature = input("Testing temperature: ")
        check_temperature(temperature)
        print()
        i += 1

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
