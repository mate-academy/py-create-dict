def create_dict(*args):
    # write your code here
    dict2 = {}

    for i, element in enumerate(args):
        if isinstance(element, (list, dict, set)):
            print(f"Cannot add {element} to the dict!")
        elif isinstance(element, tuple):
            for j in element:
                if isinstance(j, (list, dict, set)):
                    print(f"Cannot add {element} to the dict!")
                    break
            else:
                dict2[element] = i
        else:
            dict2[element] = i

    return dict2
