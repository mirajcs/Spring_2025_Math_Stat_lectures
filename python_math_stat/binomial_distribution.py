import matplotlib.pyplot as plt
from math import comb

def miraj_binomial_distribution(n, p):
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
