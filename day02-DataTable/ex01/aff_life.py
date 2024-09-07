from load_csv import load


def main():
    path = '../csv/life_expectancy_years.csv'
    life_expect = load(path)
    if life_expect is None:
        return
    title: str = "France Life expectancy Projections"
    ylabel: str = "Life expectancy"
    xlabel: str = "Year"
    life_expect = life_expect.set_index('country')
    life_expect.loc['France'].plot(title=title, ylabel=ylabel, xlabel=xlabel)


if __name__ == '__main__':
    main()
