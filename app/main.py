def create_dict(*args):
    my_dict = {}
    for index, element in enumerate(args):
        if isinstance(element, (list, set, dict)):
            print(f'Cannot add {element} to the dict!')
        elif isinstance(element, (list, tuple, set, dict)):
            for j in element:
                if isinstance(j, (list, dict, set)):
                    print(f'Cannot add {element} to the dict!')
                    break
            else:
                my_dict[element] = index
        else:
            my_dict[element] = index
    return my_dict
