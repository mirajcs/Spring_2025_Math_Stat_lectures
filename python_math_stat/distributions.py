import numpy as np
import matplotlib.pyplot as plt
from math import comb
import scipy.stats as stats

def miraj_binomial_distribution_pmf(n, p):
    """
    Plots the binomial distribution for a given number of trials (n) and probability (p).
    
    :param n: Number of trials (integer)
    :param p: Probability of success in a single trial (float, 0 ≤ p ≤ 1)
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")
    
    # Compute binomial probabilities for all k from 0 to n
    k_values = list(range(n + 1))
    probabilities = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in k_values]

    # Plot the binomial distribution
    #plt.figure(figsize=(8, 5))
    plt.bar(k_values, probabilities, color='skyblue', edgecolor='black')
    plt.xlabel("Number of Successes (k)")
    plt.ylabel("Probability")
    plt.title(f"Binomial Distribution (n={n}, p={p})")
    plt.xticks(k_values)
    plt.xticks(rotation=90)
    plt.grid(axis="y", linestyle="--", alpha=0.1)
    plt.show()



def plot_geometric_pmf(p, k_max=15):
    """
    Plots the Probability Mass Function (PMF) of a geometric distribution.
    
    Parameters:
    - p: Probability of success
    - k_max: Maximum number of trials to display (default is 15)
    """


def miraj_geometric_distribution_pmf(p, k_max=15):
    k_values = np.arange(1, k_max + 1)  # Values from 1 to k_max
    pmf_values = stats.geom.pmf(k_values, p)

    plt.figure(figsize=(7, 5))
    plt.stem(k_values, pmf_values)
    plt.xlabel('k (Number of Trials)')
    plt.ylabel('P(X=k)')
    plt.title(f'Geometric PMF (p={p})')
    #plt.grid()
    plt.show()