import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

# Number of investors
M = 5

# Number of assets in the portfolio
N = 10

initial_weights = np.random.rand(M, N)
initial_weights /= np.sum(initial_weights, axis=1, keepdims=True)  # Normalize to ensure weights sum to 1

simulated_returns = np.random.rand(M, N)
simulated_sigmas = np.random.rand(M, N)

global_variable = np.mean(simulated_returns)

rho = 0.7  # Penalty parameter
alpha = 1  # Parameter controlling the impact of the coupling term
max_iterations = 100  
epsilon = 1e-6  

def admm_solver(simulated_returns, simulated_sigmas, rho, alpha, max_iterations, epsilon):
    # Define variables
    W = cp.Variable((M, N))
    Z = cp.Variable(N)

    def local_cost_function(W_i, R_i, Sigma_i):
        return -cp.sum(cp.multiply(R_i, W_i)) + cp.quad_form(W_i, Sigma_i) + alpha * cp.abs(cp.sum(cp.multiply(R_i, W_i)) - global_variable)

    # ADMM update steps
    W_history = []
    for iteration in range(max_iterations):
        # Update W_i for each investor
        normalized_weights = []
        for i in range(M):
            local_objective = local_cost_function(W[i], simulated_returns[i], np.diag(simulated_sigmas[i]))
            regularization_term = (rho / 2) * cp.norm(W[i] - Z, 2)**2
            constraints = [cp.sum(W[i]) == 1]

            # Separate the objective and constraints
            objective = cp.Minimize(local_objective + regularization_term)
            problem = cp.Problem(objective, constraints)

            problem.solve()
            normalized_weights.append(W[i].value / np.sum(W[i].value))  # Normalize weights

        W_history.append(normalized_weights)

        # Update Z
        Z.value = np.mean([w for w in normalized_weights], axis=0)

        # Print current iteration's portfolio weights
        print(f"Iteration {iteration + 1} - Portfolio Weights:")
        for i in range(M):
            print(f"Investor {i + 1}: {normalized_weights[i]}")

    return W_history, Z.value
W_history, Z_result = admm_solver(simulated_returns, simulated_sigmas, rho, alpha, max_iterations, epsilon)

average_weights = np.mean(W_history, axis=(0, 1))
plt.figure(figsize=(12, 8))
plt.plot(range(1, len(average_weights) + 1), average_weights, label="Average Portfolio Weight")
plt.xlabel("Asset Index")
plt.ylabel("Portfolio Weight")
plt.title("Average Portfolio Weight Evolution")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(range(1, len(objective_values) + 1), objective_values, label="Main Objective Function Value")
plt.xlabel("Iteration")
plt.ylabel("Objective Function Value")
plt.title("Main Objective Function Value Evolution")
plt.legend()
plt.grid(True)
plt.show()
