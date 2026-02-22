def ft_count_harvest_recursive(t=1,
                               counter=int(input("Days until harvest: "))):
    if counter > 0:
        day = counter - 1
        ft_count_harvest_recursive(0, day)
        print(f"Day {counter}")
        if t == 1:
            print("Harvest time!")
