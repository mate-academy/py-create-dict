def create_dict(*args):
    result = {}
    for i, argument in enumerate(args):
        if isinstance(argument, (list, dict, set)
                        or argument is None or type(argument) == 'function'):
            print(f"Cannot add {argument} to the dict!")
        else:
            result[argument] = i

    return result
