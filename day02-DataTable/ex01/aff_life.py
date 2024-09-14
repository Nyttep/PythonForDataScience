from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def main():
    path = '../csv/life_expectancy_years.csv'
    life_expect = load(path)
    if life_expect is None:
        return
    title: str = "France Life expectancy Projections"
    ylabel: str = "Life expectancy"
    xlabel: str = "Year"
    xticks: np.ndarray = np.arange(0, 281, 40)
    life_expect = life_expect.set_index('country')
    life_expect.loc['France'].plot(
        title=title,
        ylabel=ylabel,
        xlabel=xlabel,
        xticks=xticks)
    plt.show()


if __name__ == '__main__':
    main()
