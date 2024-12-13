from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwargs: Any):
            nonlocal count
            if count < limit:
                function()
            else:
                print(f"Error: <function {function.__name__} at {hex(id(function))}>")
            count += 1
        
        return limit_function

    return callLimiter
