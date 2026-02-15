def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    dic = {
        "name": seed_type,
        "qtd": quantity,
        "pack": unit
    }
    ext = "available"
    type = dic["name"].capitalize()
    qtd = dic["qtd"]
    pack = dic["pack"]
    if dic["pack"] == "grams":
        ext = "total"
    if dic["pack"] == "area":
        ext = "meters"
        print(f"{type} seed: covers {qtd} square {ext}")
    else:
        print(f"{type} seed: {qtd} {pack} {ext}")
