import types


def create_dict(*args):
    result_dict = {}
    for n, element in enumerate(args):
        if isinstance(element, (str, float, int, bool)) \
                or isinstance(element, types.FunctionType) or element is None:
            result_dict[element] = n
        elif isinstance(element, tuple):
            for el in element:
                if isinstance(el, (set, list, dict)):
                    print(f"Cannot add {element} to the dict!")
                    break
            else:
                result_dict[element] = n
        else:
            print(f"Cannot add {element} to the dict!")
    return result_dict
