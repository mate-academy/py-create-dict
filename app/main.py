def create_dict(*args):

    result = {}

    for i in range(len(args)):
        if not isinstance(args[i], (list, dict, set)):
            if isinstance(args[i], tuple):
                count = 0
                for item in args[i]:
                    if isinstance(item, (list, dict, set)):
                        print(f"Cannot add {args[i]} to the dict!")
                        count = 1
                        break
                if count == 0:
                    result[args[i]] = i
            else:
                result[args[i]] = i

        else:
            print(f"Cannot add {args[i]} to the dict!")

    return result
