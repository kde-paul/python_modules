import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    try:
        if not sys.argv[1:]:
            raise ValueError()
        else:
            print(f"Program name: {sys.argv[0]}")
            print(f"Arguments received: {len(sys.argv) - 1}")
            counter = 1
            for arg in sys.argv[1:]:
                print(f"Argument {counter}: {arg}")
                counter += 1
            print(f"Total arguments: {len(sys.argv)}")
    except ValueError:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
