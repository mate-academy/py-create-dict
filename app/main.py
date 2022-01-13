def create_dict(*args):
    result = {}
    message = "Cannot add {} to the dict!"

    for index, item in enumerate(args):
        if isinstance(item, (list, set, dict)):
            print(message.format(item))
        elif isinstance(item, tuple):

            for j in item:
                if isinstance(j, (list, set, dict)):
                    print(message.format(item))
                    break

            else:
                result.update({item: index})

        else:
            result.update({item: index})

    return result
