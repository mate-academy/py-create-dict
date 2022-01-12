def create_dict(*args):
    out = {}
    for index, key in enumerate(args):
        # if callable(key): ?
        #     continue      ?
        if isinstance(key, (int, float, str, bool)):
            out[key] = index
            continue
        if isinstance(key, tuple):
            if not any([isinstance(key0, (set, list)) for key0 in key]):
                out[key] = index
                continue
        print(f"Cannot add {key} to the dict!")
    return out