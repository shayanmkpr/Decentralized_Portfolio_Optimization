# Decentralized Portfolio Optimization

This repository explores decentralized portfolio optimization problems and employs two optimization approaches: the Primal Decomposition Method and the Alternating Direction Method of Multipliers (ADMM). Additionally, a variant of ADMM, the Fast ADMM, is introduced for enhanced convergence speed.

---

## Centralized Portfolio Optimization

- **Objective**: Maximize overall portfolio performance considering individual and collective goals.
- **Decision Variables**: Portfolio weights, simulated returns, simulated standard deviations, and an adjustable parameter.
- **Constraints**:  
  1. The sum of portfolio weights must equal 1.  
  2. Portfolio weights must be non-negative.

---

## Primal Decomposition Method

1. Decompose the global objective into individual local cost functions for each investor.  
2. Local cost functions include terms for:  
   - Expected portfolio return.  
   - Portfolio risk.  
   - A coupling term involving the global variable.  
3. Iterative updates: Each investor independently optimizes their local cost function.

---

## ADMM Algorithm

1. Formulate the decentralized problem with a cost function for each investor, including terms for:  
   - Expected portfolio return.  
   - Portfolio risk.  
   - A coupling term.  
2. Use the augmented Lagrangian formulation and variable splitting for efficiency.  
3. Iterative update steps include:  
   - Optimizing local decision variables.  
   - Updating the consensus variable.  
   - Adjusting dual variables.

---

## Fast ADMM Algorithm

1. Modify the standard ADMM with variable splitting for accelerated convergence.  
2. Introduce auxiliary variables for original variables.  
3. Iterative update steps include:  
   - Optimizing original and auxiliary variables.  
   - Updating the consensus variable.  
   - Adjusting dual variables.

---

## Results

1. Visualize convergence for different algorithms and varying numbers of investors.  
2. Display the average distribution of portfolios.  
3. Analyze the impact of parameters such as alpha and rho on convergence.
