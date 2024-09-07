import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''load(path: str) -> pd.DataFrame

Load a csv file from the given path and return a pandas DataFrame.
Return None if the file is not found or if any error occured.
'''
    try:
        csv = pd.read_csv(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    print(f"Loading dataset of dimensions {csv.shape}")
    return csv
