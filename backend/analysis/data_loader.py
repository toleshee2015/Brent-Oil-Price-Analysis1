import pandas as pd


def load_data(file_path):
    """
    Load Brent oil prices dataset.
    """

    df = pd.read_csv(r"C:\Users\Soret\Downloads\BrentOilPrices.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df.sort_values("Date", inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df