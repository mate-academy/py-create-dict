def create_dict(*args):
    result = {}

    for x, y in enumerate(args):
        if isinstance(y, (list, dict, set)):
            print(f"Cannot add {y} to the dict!")
            continue
        result[y] = x

    return result
