import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    path = '../csv/life_expectancy_years.csv'
    life_expect = load(path).loc[:, ['country', '1900']]
    path = '../csv/income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    gdp = load(path).loc[:, ['country', '1900']]

    life_expect = life_expect.set_index('country')
    gdp = gdp.set_index('country')
    life_expect.columns = ['life_expectancy']
    gdp.columns = ['gdp']

    df = pd.concat([life_expect, gdp], axis=1)
    df.dropna(axis=0, inplace=True, how='any')

    df.plot(kind='scatter', x='gdp', y='life_expectancy', logx=True, s=35)
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.title("1900")
    plt.xticks([300, 1000, 10000], [300, "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
