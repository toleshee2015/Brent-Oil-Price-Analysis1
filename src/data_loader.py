import pandas as pd

def load_data(file_path="data/BrentOilPrices.csv"):

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    df.sort_values("Date", inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df