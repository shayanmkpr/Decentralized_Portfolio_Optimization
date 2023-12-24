import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

def fast_admm_solver(simulated_returns, simulated_sigmas, rho, alpha, max_iterations, epsilon):
    M, N = simulated_returns.shape
    W = [cp.Variable(N) for _ in range(M)]
    P = [cp.Variable(N) for _ in range(M)]
    Z = cp.Variable(N)
    U = [cp.Variable(N) for _ in range(M)]

    global_objective = sum([-simulated_returns[i] @ W[i] + 0.1 * cp.quad_form(W[i], np.diag(simulated_sigmas[i])) +
                            alpha * cp.norm1(simulated_returns[i] @ W[i] - sum(simulated_returns[j] @ W[j] for j in range(M)) / M) for i in range(M)])

    augmented_lagrangian = global_objective
    for i in range(M):
        augmented_lagrangian += (rho / 2) * cp.sum_squares(P[i] - W[i] + Z - U[i])

    admm_problem = cp.Problem(cp.Minimize(augmented_lagrangian))
    
    objective_values = []
    portfolio_histories = []

    for iteration in range(max_iterations):
        admm_problem.solve()

        for i in range(M):
            # Update W_i and P_i
            W[i].value = P[i].value
            P[i].value = (W[i].value + U[i].value + Z.value) / 3

        # Update Z
        Z.value = np.mean([P[i].value + U[i].value for i in range(M)], axis=0)

        # Update U_i for each investor
        for i in range(M):
            U[i].value = U[i].value + (P[i].value - Z.value)

        # Convergence check
        r_norm = np.mean([np.linalg.norm(P[i].value - Z.value) for i in range(M)])
        s_norm = rho * np.linalg.norm(Z.value - Z.value)

        objective_values.append(global_objective.value)
        portfolio_histories.append([W[i].value.tolist() for i in range(M)])

        print(f"Iteration {iteration + 1} - Portfolio Weights:")
        for i in range(M):
            print(f"Investor {i + 1}: {W[i].value}")

        if max(r_norm, s_norm) < epsilon:
            print("Converged.")
            break

    return portfolio_histories, Z.value, objective_values

# Example usage:
M = 5
N = 10
simulated_returns = np.random.rand(M, N)
simulated_sigmas = np.random.rand(M, N)
rho = 0.8
alpha = 1
max_iterations = 100
epsilon = 1e-6
portfolio_histories, Z_result, objective_values = fast_admm_solver(simulated_returns, simulated_sigmas, rho, alpha, max_iterations, epsilon)

# Plot the main objective function value over iterations
plt.figure(figsize=(12, 8))
plt.plot(range(1, len(objective_values) + 1), objective_values, label="Main Objective Function")
plt.xlabel("Iteration")
plt.ylabel("Objective Function Value")
plt.title("Main Objective Function Evolution")
plt.legend()
plt.grid(True)
plt.show()
