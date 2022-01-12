def create_dict(*args):
    for element in args:
        if isinstance(element, (list, dict, set)):
            print(f'Cannot add {element} to the dict!')
    return {data: index for index, data in enumerate(args)
            if not isinstance(data, (list, dict, set))}
