# Create dict

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

### Task

You already know, that not all data types can be used as a keys
in dictionary in Python. But someone, who pass arguments to function
`create_dict` does not. You need to help him:

Write `create_dict` function, which will receive as many arguments as needed
and create a dictionary, in which keys are these arguments (each argument is different key) provided to the function
and values are the positions of these arguments.

Of course, not all arguments provided will be accepted for dict creation.
Print `f"Cannot add {argument} to the dict!"` for each argument, that is not accepted.

It is agreed, that arguments provided to `create_dict` function will be
only of next types: `int`, `float`, `str`, `bool`, `NoneType`, `list`, `tuple`, `set`, `dict`, `function`.

Also in this task, you should not use `hash` function or `try/except` constructions.

Hint: use `isinstance`.

Examples:
```python
print(create_dict(7, 1, 3))
# {7: 0, 1: 1, 3: 2}
print(create_dict(3, [1, 2], 5))
# Cannot add [1, 2] to the dict!
# {3: 0, 5: 2}
print(create_dict(3, (1, 2), 5))
# {3: 0, (1, 2): 1, 5: 2}
```
