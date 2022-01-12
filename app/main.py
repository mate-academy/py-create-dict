import types


def create_dict(*args):
    list_arg = [arg for arg in args]
    result_dict = {}
    for n, element in enumerate(list_arg):
        if isinstance(element, (str, float, int, tuple, bool)) \
                or isinstance(element, types.FunctionType) or element is None:
            result_dict[element] = n
        else:
            print(f"Cannot add {element} to the dict!")

    return result_dict
