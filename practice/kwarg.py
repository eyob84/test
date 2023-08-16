def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, a='apple', b='banana')
# *args: Allows you to pass a variable number of non-keyword arguments to a function.
# It collects the extra positional arguments as a tuple.

# **kwargs: Allows you to pass a variable number of keyword arguments to a function.
    #   It collects the extra keyword arguments as a dictionary.