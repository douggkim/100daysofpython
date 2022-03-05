# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"Name of the function : {function.__name__}")
        for arg in args:
            print(f"Variables Used for the function : {arg} ")
        function(args[0], args[1])

    return wrapper


# Use the decorator 👇

@logging_decorator
def print_name(var_a, var_b):
    print(f"{var_a}")
    print(f"{var_b}")


print_name("Ukraine", "Russia")
