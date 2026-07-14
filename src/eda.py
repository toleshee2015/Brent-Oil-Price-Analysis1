import numpy as np
import matplotlib.pyplot as plt


def plot_price(df):

    plt.figure(figsize=(15,6))

    plt.plot(df["Date"], df["Price"])

    plt.title("Historical Brent Oil Prices")

    plt.xlabel("Date")

    plt.ylabel("Price (USD/Barrel)")

    plt.grid(True)

    plt.show()


def compute_log_returns(df):

    df["Log_Return"] = np.log(df["Price"]).diff()

    return df


def plot_log_returns(df):

    plt.figure(figsize=(15,6))

    plt.plot(df["Date"], df["Log_Return"])

    plt.title("Daily Log Returns")

    plt.grid(True)

    plt.show()


def rolling_statistics(df):

    rolling_mean = df["Price"].rolling(30).mean()

    rolling_std = df["Price"].rolling(30).std()

    plt.figure(figsize=(15,6))

    plt.plot(df["Date"], df["Price"], label="Price")

    plt.plot(df["Date"], rolling_mean, label="30-Day Mean")

    plt.plot(df["Date"], rolling_std, label="30-Day Std")

    plt.legend()

    plt.show()