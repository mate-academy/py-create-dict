def create_dict(*args):
    result = {}
    data_dict = 0
    message = "Cannot add {} to the dict!"

    for i in args:
        if isinstance(i, (str, int, float, bool)) and i is not None or callable(i):
            result.update({i: data_dict})
        elif isinstance(i, tuple):

            for j in i:
                if isinstance(j, (list, set, dict)):
                    print(message.format(i))
                    break
            else:
                result.update({i: data_dict})
        else:
            print(message.format(i))
        data_dict += 1

    return result
