def create_dict(*args):
    out = {}
    for index, key in enumerate(args):
        if isinstance(key, (int, float, str, bool)) or callable(key) or None:
            out[key] = index
            continue
        if isinstance(key, tuple):
            if not any([isinstance(key_key, (set, list)) for key_key in key]):
                out[key] = index
                continue
        print(f"Cannot add {key} to the dict!")
    return out

    # Is it possible to leave such a construction, without (if elif else)?
    # it seems to me that in this case it increases the size of the code
