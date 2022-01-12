def create_dict(*args):
    result_dict = {}
    for n, arg in enumerate(args):
        if isinstance(arg, tuple):
            temp_list = []
            for arg2 in arg:
                if not isinstance(arg2, (list, set, dict)):
                    temp_list.append(arg2)
                    continue
                else:
                    print(f"Cannot add {arg} to the dict!")
                    temp_list = []
            if temp_list:
                tuple_temp = tuple(temp_list)
                result_dict[tuple_temp] = n
        elif not isinstance(arg, (list, set, dict)):
            result_dict[arg] = n
        else:
            print(f"Cannot add {arg} to the dict!")
    return result_dict
