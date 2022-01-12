def create_dict(*args):
    dicto = {}
    for index, arg in enumerate(args):
        if isinstance(arg, tuple):
            for arg1 in arg:
                if isinstance(arg1, (list, dict, set)):
                    print(f"Cannot add {arg1} to the dict!")
                    break
                else:
                    dicto[arg] = index
        elif isinstance(arg, (list, dict, set)):
            print(f"Cannot add {arg} to the dict!")
        else:
            dicto[arg] = index
    return dicto

    pass
