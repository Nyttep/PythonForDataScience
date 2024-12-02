from typing import Any, Callable
from numbers import Number


def ft_mean(args: list[Number]) -> float:
    if len(args) == 0:
        raise ValueError("ERROR")
    mean = sum(args) / len(args)
    return mean


def ft_median(args: list[Number]) -> float:
    if len(args) == 0:
        raise ValueError("ERROR")
    lenght = len(args)
    sort = sorted(args)
    pos = lenght // 2
    if pos == -1:
        pos = 0
    if lenght % 2 == 1:
        median = sort[pos]
    else:
        median = (sort[pos - 1] + sort[pos]) / 2
    return median


def ft_quartile(args: list[Number]) -> float:
    if len(args) == 0:
        raise ValueError("ERROR")
    lenght: int = len(args)
    sort: list[Number] = sorted(args)
    pos1: int = ((lenght + 3) // 4) - 1
    pos3: int = (((lenght * 3) + 1) // 4) - 1
    quart: list[float] = [0, 0]
    if pos1 < 0:
        pos1 = 0
    if pos1 == ((lenght + 3) // 4) - 1:
        quart[0] = sort[pos1]
    else:
        quart[0] = (sort[pos1] + sort[pos1 + 1]) / 2
    if pos3 == (((lenght * 3) + 1) // 4) - 1:
        quart[1] = sort[pos3]
    else:
        quart[1] = (sort[pos3] + sort[pos3 + 1]) / 2
    return quart


def ft_variance(args: list[Number]) -> float:
    if len(args) == 0:
        raise ValueError("ERROR")
    mean = ft_mean(args)
    deviations: list[Number] = [(x - mean)**2 for x in args]
    return ft_mean(deviations)


def ft_std(args: list[Number]) -> float:
    if len(args) == 0:
        raise ValueError("ERROR")
    return ft_variance(args)**(1/2)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Computes and prints statistical measures for the given arguments.

    Parameters:
    *args (Number): arguments containing numerical values.
    **kwargs (string): keyword arguments.
                   The keys can be anything,
                   and the values should be the function names as strings.
    Supported statistical measures:
    - mean: Computes the mean of the given values.
    - median: Computes the median of the given values.
    - quartile: Computes the quartiles of the given values.
    - var: Computes the variance of the given values.
    - std: Computes the standard deviation of the given values.
    """
    functions: dict[str, Callable] = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "var": ft_variance,
        "std": ft_std,
    }

    myargs = [x for x in args if type(x) is not str]

    for x in kwargs.values():
        try:
            res: float = functions[x](myargs)
            print(f"{x} : {res}")
        except KeyError:
            pass
        except ValueError:
            print("ERROR")
            pass
