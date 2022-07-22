def create_dict(*args):
	result = {}

	for i in range(len(args)):
		if not isinstance(args[i], (list, dict, set)):
			result.update({args[i]: i})
		else:
			print(f"Cannot add {args[i]} to the dict!")

	return result
