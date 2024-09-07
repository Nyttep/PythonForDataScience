from load_csv import load


def main():
    path = '../csv/population_total.csv'
    pop_tot = load(path)
    if pop_tot is None:
        return
    pop_tot = pop_tot.set_index('country')
    print(pop_tot)


if __name__ == '__main__':
    main()
