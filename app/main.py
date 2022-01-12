import types


def create_dict(*args):
    list_arg = [arg for arg in args]
    result_dict = {}
    for n, element in enumerate(list_arg):
        if isinstance(element, (str, float, int, tuple))\
                or isinstance(element, types.FunctionType):
            result_dict[element] = n
        else:
            print(f"Cannot add {element} to the dict!")

    return result_dict
