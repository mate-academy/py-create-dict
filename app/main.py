def create_dict(*args):
    result_dict = {}
    for n, arg in enumerate(args):
        if not isinstance(arg, list | set | dict):
            try:
                result_dict[arg] = n
            except TypeError:
                print(f"Cannot add {arg} to the dict!")
        else:
            print(f"Cannot add {arg} to the dict!")
    return result_dict
