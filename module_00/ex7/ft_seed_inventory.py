def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    dic = {
        "name": seed_type,
        "qtd": quantity,
        "pack": unit
    }
    ext = "available"
    type = dic["name"].capitalize()
    if dic["pack"] == "area":
        ext = "meters"
        print(f"{type} seed: covers {dic["qtd"]} square {ext}")
        return
    elif dic["pack"] == "grams":
        ext = "total"
    print(f"{type} seed: {dic["qtd"]} {dic["pack"]} {ext}")
