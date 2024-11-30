from typing import Any
from numbers import Number


def ft_mean(args: list[Number]) -> None:
    mean = sum(args) / len(args)
    print(f"mean : {mean}")


def ft_median(args: list[Number]) -> None:
    lenght = len(args)
    sort = sorted(args)
    pos = lenght // 2
    if pos == -1 :
        pos = 0
    if lenght % 2 == 1:
        median = sort[pos]
    else:
        median = (sort[pos - 1] +  sort[pos]) / 2
    print(f"median : {median}")


def ft_quartile(args: list[Number]) -> None:
    lenght: int = len(args)
    sort: list[Number] = sorted(args)
    pos1: int = ((lenght + 3) // 4) - 1
    pos3: int = (((lenght * 3) + 1) // 4) - 1
    quart: list[float] = [0, 0]
    if pos1 < 0 :
        pos1 = 0
    if pos1 == ((lenght + 3) // 4) - 1 :
        quart[0] = sort[pos1]
    else:
        quart[0] = (sort[pos1] + sort[pos1 + 1]) / 2
    if pos3 == (((lenght * 3) + 1) // 4) - 1 :
        quart[1] = sort[pos3]
    else:
        quart[1] = (sort[pos3] + sort[pos3 + 1]) / 2
    print(f"quartile : {quart}")
    pass


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    functions: dict[str, function] = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
    }
    
    myargs = [x for x in args if type(x) != str]

    if len(myargs) == 0:
        return

    for x in kwargs.values():
        try:
            functions[x](myargs)
        except KeyError:
            pass
