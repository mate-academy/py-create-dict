def create_dict(*args):
    new_dict = {}
    for i in range(len(args)):
        if type(args[i]) in [list, set, dict]:
            print(f"Cannot add {args[i]} to the dict!")
        elif type(args[i]) is tuple:
            for arg in args[i]:
                if type(arg) is list:
                    print(f"Cannot add {args[i]} to the dict!")
                    break
            else:
                new_dict[args[i]] = i
        else:
            new_dict[args[i]] = i
    return new_dict
