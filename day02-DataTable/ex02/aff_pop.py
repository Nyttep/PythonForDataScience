from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def main():
    path = '../csv/population_total.csv'
    pop_tot = load(path)
    pop_tot = pop_tot.set_index('country')
    pop_tot = pop_tot.T  # transpose the dataframe (make the rows the culumns)
    pop_tot = pop_tot.loc[:"2050", ["France", "Belgium"]]
    mapping = str.maketrans({'k': 'e3', 'M': 'e6', 'B': 'e9'})
    pop_tot = pop_tot.map(lambda y: y.translate(mapping))
    pop_tot = pop_tot.astype(float).astype(int)
    title = "Population Projections"
    ylabel = "Population"
    xlabel = "Year"
    xticks = np.arange(0, 251, 40)
    pop_tot.plot(title=title, ylabel=ylabel, xlabel=xlabel, xticks=xticks)
    plt.legend(loc='lower right')
    yticks = np.arange(20000000, 70000000, 20000000)
    ylabels = ['20M', '40M', '60M']
    plt.yticks(ticks=yticks, labels=ylabels)
    plt.show()


if __name__ == '__main__':
    main()
