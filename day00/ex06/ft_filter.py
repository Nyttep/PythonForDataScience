def ft_filter(func, iterable) -> iter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is None:
        return iter([item for item in iterable if item is True])
    else:
        return iter([item for item in iterable if func(item) is True])