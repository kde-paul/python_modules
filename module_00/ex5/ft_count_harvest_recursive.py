def ft_count_harvest_recursive(counter=int(input("Days until harvest: "))):
    if counter > 0:
        day = counter - 1
        ft_count_harvest_recursive(day)
        print(f"Day {counter}")
