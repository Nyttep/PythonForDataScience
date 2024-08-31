from os import get_terminal_size
import sys

def ft_tqdm(lst: range) -> None:
    term_width = get_terminal_size().columns
    white = "\033[47m \033[m"
    # white = "="
    black = " "
    total = len(lst)
    bar_length = term_width - (34 + len(str(total) * 2))
    i = 0
    for elem in lst:
        i += 1
        bar_progress = (int)((i / total) * bar_length)
        white_bar = white * bar_progress
        black_bar = black * abs(bar_progress - bar_length)
        print("{:>4.0%}|{}{}| {}/{}".format(i/total, white_bar, black_bar, i, total), end="\r", flush=True)
        yield elem
