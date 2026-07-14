import pymc as pm
import numpy as np
import arviz as az
import pandas as pd
import time
import os


def run_bayesian_model(df):

    y = df["Price"].values
    n = len(y)

    print(f"Number of observations: {n}")

    with pm.Model() as model:

        # Change point
        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n - 1
        )

        # Mean before change point
        mu1 = pm.Normal(
            "mu1",
            mu=np.mean(y),
            sigma=np.std(y)
        )

        # Mean after change point
        mu2 = pm.Normal(
            "mu2",
            mu=np.mean(y),
            sigma=np.std(y)
        )

        # Common standard deviation
        sigma = pm.HalfNormal(
            "sigma",
            sigma=np.std(y)
        )

        # Switch function
        mu = pm.math.switch(
            np.arange(n) < tau,
            mu1,
            mu2
        )

        # Likelihood
        pm.Normal(
            "obs",
            mu=mu,
            sigma=sigma,
            observed=y
        )

        print("Starting MCMC sampling...")

        start = time.time()

        trace = pm.sample(
            draws=100,
            tune=100,
            chains=2,
            cores=1,
            target_accept=0.90,
            random_seed=42,
            progressbar=True,
            return_inferencedata=True
        )

        end = time.time()

        print(f"Sampling completed in {end-start:.2f} seconds.")

    # Create summary
    summary = az.summary(trace)

    # Create output folder if it doesn't exist
    os.makedirs("backend/data", exist_ok=True)

    # Save summary
    summary.to_csv("backend/data/changepoint_results.csv")

    print("Change point results saved to backend/data/changepoint_results.csv")

    return trace


if __name__ == "__main__":

    from data_loader import load_data

    df = load_data("data/BrentOilPrices.csv")

    trace = run_bayesian_model(df)

    print(az.summary(trace))