import arviz as az

import matplotlib.pyplot as plt


def summary(trace):

    print(az.summary(trace))


def trace_plot(trace):

    az.plot_trace(trace)

    plt.show()


def posterior_tau(trace):

    az.plot_posterior(
        trace,
        var_names=["tau"]
    )

    plt.show()


def posterior_means(trace):

    az.plot_posterior(
        trace,
        var_names=["mu1","mu2"]
    )

    plt.show()