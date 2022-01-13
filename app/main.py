def create_dict(*args):
    res_dict = {}
    is_not_tuple = True

    for iterator, value in enumerate(args):

        if (
            isinstance(value, (list, set, dict))
        ):
            print(f"Cannot add {value} to the dict!")
            continue
        if isinstance(value, tuple):
            for j in value:
                if (
                    isinstance(j, (list, dict))
                ):
                    print(f"Cannot add {value} to the dict!")
                    is_not_tuple = False
                    break
        if is_not_tuple:
            res_dict[value] = iterator

        is_not_tuple = True
    return res_dict
