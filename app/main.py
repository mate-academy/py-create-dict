def create_dict(*args):
    result_dict = {}
    for n, arg in enumerate(args):
        if isinstance(arg, (list, dict, set)):
            print(f"Cannot add {arg} to the dict!")
        elif isinstance(arg, tuple):
            h = True
            for arg2 in arg:
                if isinstance(arg2, (list, dict, set)):
                    h = False
                    print(f"Cannot add {arg} to the dict!")
                    break
                if h:
                    result_dict[arg] = n
        else:
            result_dict[arg] = n

    return result_dict
