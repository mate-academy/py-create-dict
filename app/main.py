def create_dict(*args):
    result = {}
    for index, arg in enumerate(args):
        if isinstance(arg, (list, set, dict)):
            print(f"Cannot add {arg} to the dict!")
        elif isinstance(arg, tuple):
            is_hashable = True

            for item in arg:
                if isinstance(item, (list, set, dict)):
                    is_hashable = False
                    print(f"Cannot add {item} to the dict!")
                    break

            if is_hashable:
                result[arg] = index

        else:
            result[arg] = index

    return result
