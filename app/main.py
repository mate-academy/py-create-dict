import types


def create_dict(*args):
    dictionary = {}
    for argument in args:
        if not isinstance(argument, (int, float, str, tuple, types.FunctionType)):
            print(f"Cannot add {argument} to the dict!")
        else:
            dictionary[argument] = args.index(argument)
    return dictionary
