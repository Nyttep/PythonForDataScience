from typing import Any


def callLimit(limit: int):
    cout = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwargs: Any):
            pass
