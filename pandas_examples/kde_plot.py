"""
normal-distribution-demo.py

This demo was originally written to demonstrate how different sample sizes will affect your results.
It also functions as a nice example of how a kernel density estimate can be added to a plot to
help visualize results.

See also:
    The Galton Board (will help you understand the central limit theorem!
    https://www.youtube.com/watch?v=EvHiee7gs9Y
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Parameters
mu, sigma = 100, 15  # Mean and standard deviation of the normal distribution
sample_sizes = [100, 1000, 10000, 100000]  # Different sample sizes

# Create subplots
fig, axs = plt.subplots(len(sample_sizes), figsize=(8, 6))

# Generate samples and plot histograms for each sample size
for i, size in enumerate(sample_sizes):
    # Generate random samples from the normal distribution, using our mean and std
    samples = np.random.normal(mu, sigma, size)

    # Plot histogram with a kernel density estimate plotted alongside the distribution.
    # This shows the estimated distribution, which should look more like the normal distribution
    sns.histplot(samples, bins=30, kde=True, ax=axs[i])
    axs[i].set_title(f'Sample Size: {size}')
    axs[i].set_xlabel('Value')
    axs[i].set_ylabel('Density')

plt.tight_layout()

# Save the plot to a file
plt.savefig('sample_distribution.png')

plt.show()