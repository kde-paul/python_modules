import math


def parse(coordinates: str) -> tuple:
    try:
        lst = coordinates.split(',')
        p_one = int(lst[0])
        p_two = int(lst[1])
        p_three = int(lst[2])
        return tuple((p_one, p_two, p_three))
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(f"Error details - Type: {type(error).__name__}, Args: {error.args}")

def calc_distance(base: tuple, coordinates: tuple) -> float:
    return math.sqrt((coordinates[0] - base[0])**2
                     + (coordinates[1] - base[1])**2
                     + (coordinates[2] - base[2])**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    base = tuple((0, 0, 0))
    tup = tuple((10, 20, 5))
    print(f"Position created: ({tup[0]}, {tup[1]}, {tup[2]})")
    print(f"Distance between ({base[0]}, {base[1]}, {base[0]}) \
and ({tup[0]}, {tup[1]}, {tup[2]}): {calc_distance(base, tup):.2f}\n")

    coordinates = "3,4,0"
    print("Parsing coordinates:", coordinates)
    parsed = parse(coordinates)
    print("Parsed position:", parsed)
    print(f"Distance Between ({base[0]}, {base[1]}, {base[0]}) \
and ({parsed[0]}, {parsed[1]}, {parsed[2]}): {calc_distance(base, parsed)}\n")

    invalid = "abc,def,ghi"
    print("Parsing invalid coordinates:", invalid)
    parse(invalid)

    print("\nUnpacking demonstration:")
    p_one = 3
    p_two = 4
    p_three = 0
    player = parse(f"{p_one},{p_two},{p_three}")
    print(f"Player at x={p_one}, y={p_two}, z={p_three}")
    print(f"Coordinates: X={player[0]}, Y={player[1]}, Z={player[2]}")
