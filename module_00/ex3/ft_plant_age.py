def ft_plant_age():
    plant_day = int(input("Enter plant age in days: "))
    if plant_day > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
