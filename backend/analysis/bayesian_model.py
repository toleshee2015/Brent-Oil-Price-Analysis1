import pymc as pm

import numpy as np

import arviz as az


def run_bayesian_model(df):

    y = df["Price"].values

    n = len(y)

    with pm.Model() as model:

        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n-1
        )

        mu1 = pm.Normal(
            "mu1",
            mu=np.mean(y),
            sigma=np.std(y)
        )

        mu2 = pm.Normal(
            "mu2",
            mu=np.mean(y),
            sigma=np.std(y)
        )

        sigma = pm.HalfNormal(
            "sigma",
            sigma=np.std(y)
        )

        mu = pm.math.switch(
            np.arange(n) < tau,
            mu1,
            mu2
        )

        pm.Normal(
            "obs",
            mu=mu,
            sigma=sigma,
            observed=y
        )

        trace = pm.sample(
            draws=2000,
            tune=1000,
            chains=2,
            cores=1,
            target_accept=0.95,
            random_seed=42,
            return_inferencedata=True
        )

    return trace