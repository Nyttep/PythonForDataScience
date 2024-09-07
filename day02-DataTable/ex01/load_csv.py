import pandas as pd


def load(path: str) -> pd.DataFrame:
    csv = pd.read_csv(path)
    print(f"Loading dataset of dimensions {csv.shape}")
    return csv
