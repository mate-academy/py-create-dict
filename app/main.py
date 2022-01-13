def create_dict(*args):

    new_dict = {}

    for index, argument in enumerate(args):

        if isinstance(argument, (set, list, dict)):
            print(f"Cannot add {argument} to the dict!")

        elif isinstance(argument, tuple):
            for i in argument:
                if isinstance(i, (set, list, set)):
                    print(f"Cannot add {argument} to the dict!")
                    break
            else:
                new_dict[argument] = index
        else:
            new_dict[argument] = index

    return new_dict
