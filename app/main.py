def create_dict(*args):
    res_dict = {}
    for counter, i in enumerate(args):
        if isinstance(i, (int, str, float, bool)) or callable(i) or i is None or check(i):
            res_dict.update({i: counter})
        else:
            print(f"Cannot add {i} to the dict!")
    return res_dict


def check(param):
    if isinstance(param, (int, str, float, bool)) or callable(param) or param is None:
        return True
    if isinstance(param, tuple):
        return all(check(j) for j in param)
    return False
