import time


def generator(times: int):
    if times % 2 == 0:
        player = "bob"
        level = 12
        event = "found treasure"
    elif times % 3 == 0:
        player = "charlie"
        level = 8
        event = "leveled up"
    else:
        player = "alice"
        level = 5
        event = "killed monster"
    yield player, level, event


def fibonacci(sequence: int):
    previous = 0
    current = 1
    seq_counter = 0
    while seq_counter < sequence:
        yield previous
        tmp = previous
        previous = current
        current = tmp + previous
        seq_counter += 1


def prime(numbers: int):
    prime = 2
    counter = 0
    while counter < numbers:
        number = 2
        while number < prime:
            if prime % number == 0:
                prime += 1
                number = 2
            number += 1
        yield prime
        prime += 1
        counter += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    events = 1000
    print(f"Processing {events} game events...")
    counter = 1
    high_lvl_players = 0
    total_treasure = 0
    total_lvlup = 0
    process_time = time.time()
    while counter < events:
        player, level, event = next(iter(generator(counter)))
        if counter < 4:
            print(f"Event {counter}: Player {player} (level {level}) {event}")
        counter += 1
        if level >= 10:
            high_lvl_players += 1
        if event == "found treasure":
            total_treasure += 1
        elif event == "leveled up":
            total_lvlup += 1
    process_time = time.time() - process_time
    print("...")

    print("\n=== Stream Analytics ===")
    print("Total events processed:", counter)
    print("High-level players (10+):", high_lvl_players)
    print("Treasure events:", total_treasure)
    print("Level-up events:", total_lvlup)

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {process_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib_seq = 10
    print(f"Fibonacci sequence (first {fib_seq}): ", end="")
    counter = 0
    for fib in fibonacci(fib_seq):
        print(fib, end="")
        if counter < fib_seq - 1:
            print(", ", end="")
        counter += 1
    print()
    primes = 5
    counter = 0
    print(f"Prime numbers (first {primes}): ", end="")
    for primer in prime(primes):
        print(primer, end="")
        if counter < primes - 1:
            print(", ", end="")
        counter += 1
    print()
