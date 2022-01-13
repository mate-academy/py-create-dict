def create_dict(*args):
    dicto = {}
    for index, arg in enumerate(args):
<<<<<<< HEAD
        if isinstance(arg, (set, list, dict)):
            print(f"Cannot add {arg} to the dict!")
        elif not isinstance(arg, (set, list, dict)):
            dicto[arg] = index
        elif isinstance(arg, tuple):
            for i in arg:
                if isinstance(i, (set, list, dict)):
                    print(f"Cannot add {arg} to the dict!")
                    break
                else:
                    dicto[arg] = index
    return dicto
=======
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
>>>>>>> 6f01e4170a80eb2b28a036e1d8c1dd3817361b7b
