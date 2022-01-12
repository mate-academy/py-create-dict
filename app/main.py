def is_valid(el):
    if isinstance(el, (int, float, str, bool)) or el is None or callable(el):
        return True
    elif isinstance(el, tuple):
        return all(is_valid(e) for e in el)
    return False


def create_dict(*args):
    result = dict()

    for i in range(len(args)):
        if is_valid(args[i]):
            result[args[i]] = i
        else:
            print(f"Cannot add {args[i]} to the dict!")

    return result
