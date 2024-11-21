# Decentralized Portfolio Optimization

This repository explores decentralized portfolio optimization problems and employs two optimization approaches: the Primal Decomposition Method and the Alternating Direction Method of Multipliers (ADMM). Additionally, a variant of ADMM, the Fast ADMM, is introduced for enhanced convergence speed.

## Centralized Portfolio Optimization

- **Objective:** Maximize overall portfolio performance considering individual and collective goals.
- **Decision Variables:** Portfolio weights, simulated returns, simulated standard deviations, and an adjustable parameter.
- **Constraints:** Ensure the sum of portfolio weights equals 1, and weights are non-negative.

## Primal Decomposition Method

- Decompose the global objective into individual local cost functions for each investor.
- Local cost functions include terms related to expected portfolio return, portfolio risk, and a coupling term involving the global variable.
- Iterative updates: Each investor independently optimizes their local cost function.

## ADMM Algorithm

- Formulate the decentralized problem with a cost function for each investor, considering expected portfolio return, portfolio risk, and a coupling term.
- Use augmented Lagrangian formulation, variable splitting, and specialized updating rules for efficiency.
- Iterative update steps include optimizing local decision variables, updating the consensus variable, and adjusting dual variables.

## Fast ADMM Algorithm

- Modify the standard ADMM with variable splitting for accelerated convergence.
- Introduce auxiliary variables for original variables.
- Update steps include optimizing original and auxiliary variables, updating the consensus variable, and adjusting dual variables.

## Results

- Visualize convergence for different algorithms and varying numbers of investors.
- Display the average distribution of portfolios.
- Analyze the impact of parameters (e.g., α, ρ) on convergence.

## Conclusion

- Explore decentralized portfolio optimization with practical optimization methods.
- Conduct a comparative analysis of Primal Decomposition, ADMM, and Fast ADMM.
- Provide recommendations for adjusting algorithm parameters based on convergence and solution accuracy.

**Note:**
- Adjustments to local cost functions, penalty parameters, and convergence tolerances may be necessary based on specific problem characteristics.
- Code examples and detailed implementation are available in the LaTeX document.
- Visualizations provide insights into algorithm convergence and portfolio distributions.
