def create_dict(*args):
    param = list(args)
    resultd = {}
    for i in range(len(param)):
        if isinstance(param[i], (list, set, dict)):
            print(f"Cannot add {param[i]} to the dict!")
        if param[i] is None or callable(param[i]) \
                or isinstance(param[i], (int, float, str, bool)):
            resultd[param[i]] = i
        if isinstance(param[i], tuple):
            count = 0
            for j in param[i]:
                if isinstance(j, (list, set, dict)):
                    count += 1
            if count == 0:
                resultd[param[i]] = i
            else:
                print(f"Cannot add {param[i]} to the dict!")
    return resultd
