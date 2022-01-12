import types


def is_allowed_type(obj) -> bool:
    """

    :param obj:
    :return True if object has type from
    [int, float, str, bool, NoneType, list, tuple, set, dict, function]
    what can be used as dict key, otherwise false


    """
    allowed_types = [int, float, bool, str, tuple, types.FunctionType]
    return any(isinstance(obj, i) for i in allowed_types)


def check_types(*args):
    """

    :param *args:
    :return True if all of arguments and all contained data can be used as dict key,
    False otherwise:


    """
    result = True
    for arg in args:
        result = result and is_allowed_type(arg)
        if hasattr(arg, '__iter__') and not isinstance(arg, str):
            result = result and check_types(*arg)
        else:
            result = result and is_allowed_type(arg)
    return result


def create_dict(*args):
    result = {}

    for i in range(len(args)):
        if check_types(args[i]):
            result[args[i]] = i
        else:
            print(f"Cannot add {args[i]} to the dict!")

    return result





