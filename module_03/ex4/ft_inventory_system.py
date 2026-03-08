import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("No value enough")
        else:
            lst = []
            for arg in sys.argv[1:]:
                lst.append(arg.split(":"))
            dictionary = dict(lst)
            for key in dictionary:
                dictionary[key] = int(dictionary[key])
    except Exception as error:
        print("Error:", error)

    print("=== Inventory System Analysis ===\n")
    val_total = sum(dictionary.values())
    items = len(dictionary)
    print("Total items in inventory:", val_total)
    print("Unique item types:", items)

    print("\n=== Current Inventory ===")
    for key in dictionary:
        print(f"{key}: {dictionary[key] / val_total * 100:.1f}%")

    print("\n=== Inventory Statistics ===")
    most_val = -1
    most_key = ""
    for key, val in dictionary.items():
        if val > most_val:
            most_val = val
            most_key = key
    print(f"Most abundant: {most_key} ({most_val} units)")
    least_val = 2147483647
    least_key = ""
    for key, val in dictionary.items():
        if val < least_val:
            least_val = val
            least_key = key
    print(f"Least abundant: {least_key} ({least_val} units)")

    print("\n=== Item Categories ===")
    moderate = {}
    scare = {}
    for key in dictionary:
        if dictionary[key] > 3:
            moderate.update({key: dictionary[key]})
        else:
            scare.update({key: dictionary[key]})
    print("Moderate:", moderate)
    print("Scare", scare)

    print("\n=== Management Suggestions ===")
    needed = []
    for key in dictionary:
        if dictionary[key] < 2:
            needed.append(key)
    print("Restock needed: ", end="")
    print(*needed, sep=", ")

    print("\n=== Dictionary Properties Demo ===")
    all_keys = []
    for key in dictionary:
        all_keys.append(key)
    print("Dictionary keys: ", end="")
    print(*all_keys, sep=", ")
    all_vals = []
    for key in dictionary:
        all_vals.append(dictionary[key])
    print("Dictionary values: ", end="")
    print(*all_vals, sep=", ")
    lookup = "sword"
    key_state = False
    for key in dictionary:
        if lookup == key:
            key_state = True
    print(f"Sample lookup - '{lookup}' in inventory: {key_state}")
