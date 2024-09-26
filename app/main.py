def is_valid_type(items):
    if isinstance(items, (int, str, float, bool)) or items is None or callable(items):
        return True
    elif isinstance(items, tuple):
        return all([is_valid_type(item) for item in items])
    return False


def create_dict(*args):
    valid_dict = {}
    for ident, item in enumerate(args):
        if is_valid_type(item):
            valid_dict[item] = ident
        else:
            print(f"Cannot add {item} to the dict!")
    return valid_dict
