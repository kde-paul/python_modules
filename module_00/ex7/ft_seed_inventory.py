def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    dic = {
        "name": seed_type,
        "qtd": quantity,
        "pack": unit
    }
    ext = "Unknown unit type"
    type = dic["name"].capitalize()
    qtd = dic["qtd"]
    pack = dic["pack"]
    if dic["pack"] == "packets":
        ext = "available"
    if dic["pack"] == "grams":
        ext = "total"
    if dic["pack"] == "area":
        ext = "meters"
        print(f"{type} seed: covers {qtd} square {ext}")
    else:
        print(f"{type} seed: {qtd} {pack} {ext}")