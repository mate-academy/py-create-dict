def create_dict(*args):
    dicto = {}
    for index, arg in enumerate(args):
        if isinstance(arg, (set, list, dict)):
            print(f"Cannot add {arg} to the dict!")
        elif isinstance(arg, tuple):
            for i in arg:
                if isinstance(i, (set, list, dict)):
                    print(f"Cannot add {arg} to the dict!")
                    break
                else:
                    dicto[arg] = i
        elif not isinstance(arg, (set, list, dict)):
            dicto[arg] = index

        else:
            dicto[arg] = index
    return dicto
