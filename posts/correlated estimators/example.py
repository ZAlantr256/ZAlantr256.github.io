import numpy as np
from matplotlib import pyplot as plt

def simulate(trials):
    n = trials
    A_data = np.random.normal(size = (n,125))
    B_data = np.random.normal(size = (n,125))
    CD_data = np.random.normal(size = (n,200))
    C_data = CD_data[:,:190]
    D_data = CD_data[:,10:]

    mu_A = np.mean(A_data, axis = 1)
    mu_B = np.mean(B_data, axis = 1)
    mu_C = np.mean(C_data, axis = 1)
    mu_D = np.mean(D_data, axis = 1)

    return (mu_A, mu_B, mu_C, mu_D)

def plot_estimates(estimates, fs):

    bins = np.linspace(-0.4,0.4,50)
    alpha = 0.5

    fig, axes = plt.subplots(
        nrows=2,
        ncols=2,
        figsize = fs,
        sharex=True,
        sharey=True
    )

    axes[0][0].hist(estimates[0], bins = bins, alpha = alpha)
    axes[0][0].set_title(r'$\mu_{A}$')

    axes[0][1].hist(estimates[1], bins = bins, alpha = alpha)
    axes[0][1].set_title(r'$\mu_{B}$')

    axes[1][0].hist(estimates[2], bins = bins, alpha = alpha)
    axes[1][0].set_title(r'$\mu_{C}$')

    axes[1][1].hist(estimates[3], bins = bins, alpha = alpha)
    axes[1][1].set_title(r'$\mu_{D}$')

    fig.suptitle("Empirical distributions of uncombined estimators")

    for i in axes:
        for ax in i:
            ax.set_xlabel('Estimated mean')
            ax.set_ylabel('Frequency')

    plt.tight_layout()
    plt.ylim(0,120000)
    plt.show()

def make_combined(estimates):
    
    mu_uncorrelated = (estimates[0] + estimates[1])/2
    mu_correlated = (estimates[2] + estimates[3])/2

    return (mu_uncorrelated,mu_correlated)

def plot_combined(combined, fs):

    bins = np.linspace(-0.4,0.4,50)
    alpha = 0.5

    fig, axes = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(fs[0],fs[1]*(7/12)),
        sharex=True,
        sharey=True
    )

    axes[0].hist(combined[0], bins = bins, alpha = alpha)
    axes[0].set_title(r'$\mu_{uncorrelated}$')

    axes[1].hist(combined[1], bins = bins, alpha = alpha)
    axes[1].set_title(r'$\mu_{correlated}$')

    fig.suptitle("Empirical distributions of optimal combined estimators")

    for ax in axes:
        ax.set_xlabel('Estimated mean')
        ax.set_ylabel('Frequency')

    plt.tight_layout()
    plt.ylim(0,120000)
    plt.show()