def create_dict(*args):
    result_dict = {}
    for i in range(len(args)):
        if isinstance(args[i], (list, set, dict)) or args[i] is None:
            print(f"Cannot add {args[i]} to the dict!")
            continue
        else:
            result_dict.update({args[i]: i})
    return result_dict
