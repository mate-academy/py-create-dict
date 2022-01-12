def create_dict(*args):
    result_dict = {}
    for i, element in enumerate(args):
        if checker(element):
            result_dict[element] = i
        else:
            print(f"Cannot add {element} to the dict!")
    return result_dict


def checker(element):
    if isinstance(element, (str, float, int, bool)) or element is None or callable(element):
        return True
    elif isinstance(element, tuple):
        return all(checker(k) for k in element)
    return False
