from typing import Any
from numbers import Number


def ft_mean(args: list[Number]) -> None:
    mean = sum(args) / len(args)
    print(f"mean : {mean}")


def ft_median(args: list[Number]) -> None:
    lenght = len(args)
    sort = sorted(args)
    if lenght % 2 == 1:
        median = sort[lenght // 2]
    else:
        median = ft_mean(sort[(lenght // 2) - 1], sort[lenght // 2])
    print(f"median : {median}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    functions: dict[str, function] = {
        "mean": ft_mean,
        "median": ft_median,
    }

    for x in kwargs.values():
        try:
            functions[x](args)
        except KeyError:
            pass
