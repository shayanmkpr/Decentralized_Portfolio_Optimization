import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Number of investors
M = 5

# Number of assets in the portfolio
N = 100

# Set random initial portfolio weights for each investor
initial_weights = np.random.rand(M, N)
initial_weights /= np.sum(initial_weights, axis=1, keepdims=True)  # Normalize to ensure weights sum to 1

# Define investor-specific data (simulated returns and standard deviations)
simulated_returns = np.random.rand(M, N)
simulated_sigmas = np.random.rand(M, N)

# Define global variable (average return)
global_variable = np.mean(simulated_returns)

# Define local cost functions
def local_cost_function(investor_weights, investor_return, investor_sigma, alpha):
    return -np.dot(investor_return, investor_weights) + 0.1 * np.dot(investor_sigma, investor_weights) + alpha * np.abs(np.dot(investor_return, investor_weights) - global_variable)

# Define the global objective function
def global_objective(weights):
    global_return = np.dot(np.mean(simulated_returns, axis=0), weights)
    return -global_return  # Minimize negative return (maximize return)

# Lists to store rewards for each investor at each iteration
reward_history = [[] for _ in range(M)]

# Perform primal decomposition iteration
convergence_threshold = 1e-6
for iteration in range(100):  # Set the number of iterations
    # Local Optimization
    for investor in range(M):
        # Define the local objective function for the current investor
        local_objective = lambda x: local_cost_function(x, simulated_returns[investor], simulated_sigmas[investor], 1.0)

        # Perform local optimization for the current investor
        result = minimize(local_objective, initial_weights[investor], constraints={'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
        initial_weights[investor] = result.x / np.sum(result.x)  # Normalize weights

        # Append the reward (local cost) to the history
        reward_history[investor].append(local_objective(result.x))
        print(f"Iteration {iteration + 1}, Investor {investor + 1} - Reward: {reward_history[investor][-1]:.4f}")
        print("Optimal Portfolio Weights:")
        print(initial_weights[investor])
        print("\n")

    # Update Global Variable
    global_result = minimize(global_objective, np.mean(initial_weights, axis=0), constraints={'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
    global_variable = -global_result.fun  # Minimize negative global return (maximize global return)

    # Check for convergence
    if iteration > 0:  # Skip the check for the first iteration
        convergences = [np.abs(reward_history[investor][-1] - reward_history[investor][-2]) for investor in range(M)]
        if all(convergence < convergence_threshold for convergence in convergences):
            print("Converged.")
            break

# Plotting the reward history for each investor
plt.figure(figsize=(10, 6))
for investor in range(M):
    plt.plot(range(1, iteration + 2), reward_history[investor], label=f"Investor {investor + 1}")

plt.xlabel("Iteration")
plt.ylabel("Local Cost (Reward)")
plt.title("Local Cost History for Each Investor")
plt.legend()
plt.grid(True)
plt.show()
