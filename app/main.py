def create_dict(*args):
    dicto = {}
    for index, arg in enumerate(args):
        if isinstance(arg, tuple):
            for element in arg:
                if isinstance(element, (set, list, dict)):
                    print(f"Cannot add {element} to the dict!")
                    break
                else:
                    dicto[arg] = element
        if isinstance(arg, (set, list, dict, bool)):
            print(f"Cannot add {arg} to the dict!")

        elif not isinstance(arg, (set, list, dict)):
            dicto[arg] = index

        else:
            dicto[arg] = index
    return dicto
