def create_dict(*args):
    param = list(args)
    resultd = {}
    count = 0
    for i in range(len(param)):
        if isinstance(param[i], list) or isinstance(param[i], set) \
                or isinstance(param[i], dict):
            print(f"Cannot add {param[i]} to the dict!")
        if param[i] is None or callable(param[i]) \
                or isinstance(param[i], int) \
                or isinstance(param[i], float) or isinstance(param[i], str) \
                or isinstance(param[i], bool):
            resultd[param[i]] = i
        if isinstance(param[i], tuple):
            for j in param[i]:
                if isinstance(j, list) or isinstance(j, set) \
                        or isinstance(j, dict):
                    count += 1
            if count == 0:
                resultd[param[i]] = i
            else:
                print(f"Cannot add {param[i]} to the dict!")
    return resultd
