def garden_operations(type: int) -> None:
    if type == 0:
        try:
            test = "three"
            int(test)
            print(test)
        except ValueError:
            print("Testing ValueError...")
            print("Caught ValueError: invalid literal for int()")
    elif type == 1:
        try:
            r = 10 / 0
            print(r)
        except ZeroDivisionError:
            print("Testing ZeroDivisionError...")
            print("Caught ZeroDivisionError: division by zero")
    elif type == 2:
        try:
            file_to_open = "missing.txt"
            open(file_to_open, "r")
        except FileNotFoundError:
            print("Testing FileNotFoundError...")
            print("Caught FileNotFoundError: No such file'missing.txt'")
    elif type == 3:
        try:
            dict_test = {
                "plant": "rose",
                "tree": "oak"
            }
            print(f"{dict_test["_plant"]}")
        except KeyError:
            print("Testing KeyError...")
            print("Caught KeyError:'missing\\_plant'")
    elif type == 4:
        try:
            open('something.txt')
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Testing multiple errors together...")
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    i = 0
    while i < 5:
        garden_operations(i)
        print()
        i += 1

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
