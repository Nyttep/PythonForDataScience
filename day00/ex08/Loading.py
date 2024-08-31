from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    term_width = get_terminal_size().columns
    white = "\033[47m \033[m"
    black = " "
    total = len(lst)
    bar_length = term_width - (34 + len(str(total) * 2))
    i = 0
    for elem in lst:
        i += 1
        bar_progress = (int)((i / total) * bar_length)
        w_bar = white * bar_progress
        b_bar = black * abs(bar_progress - bar_length)
        txt = "{:>4.0%}|{}{}| {}/{}".format(i/total, w_bar, b_bar, i, total)
        print(txt, end="\r", flush=True)
        yield elem
