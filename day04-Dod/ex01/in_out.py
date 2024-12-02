def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Creates a closure that applies a given function to an initial value and
    then repeatedly applies the function to the result each time the closure
    is called.
    Parameters:
        x (int | float): The initial value.
        function : The function to be applied to the value.
    Returns:
        Callable: A closure that, when called, applies the function to
        the current value and returns the result.
    """
    count = 0

    def inner() -> float:
        nonlocal count

        y = function(x)
        for i in range(count):
            y = function(y)
        count += 1
        return y
    return inner
