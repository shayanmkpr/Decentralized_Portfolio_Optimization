# Decentralized Portfolio Optimization

## Overview
This repository implements a **Decentralized Portfolio Optimization** framework that solves for optimal portfolio allocations for multiple investors using mathematical optimization techniques, including the **Primal Decomposition Method**, **ADMM (Alternating Direction Method of Multipliers)**, and **Fast ADMM**. The repository includes code and documentation to simulate both centralized and decentralized approaches.

---

## Problem Description

### Key Components
- **Investors**: \( M \) independent investors, each with their own risk profile, investment goals, and constraints.
- **Assets**: \( N \) financial assets available for investment.
- **Local Variables**: Each investor allocates weights to assets in their portfolio (\( W_{ij} \)), such that:
  - \( \sum_{i=1}^{N} W_{ij} = 1 \quad \forall j \)
  - \( W \geq 0 \) (non-negativity constraint)
- **Global Objective**: Optimize overall portfolio performance while balancing individual objectives and aligning with a global goal.

---

## Centralized Optimization Formulation

The centralized objective function:

\[
\sum_{i=1}^M \left( -R_i^T W_i + 0.1 \sum_{j=1}^N W_{ij} \Sigma_{ij} W_{ij} + \alpha \sum_{j=1}^N \left| R_{ij}^T W_{ij} - \frac{1}{M} \sum_{k=1}^M R_{kj}^T W_{kj} \right| \right)
\]

### Notation
- \( W \): Portfolio weights matrix (\( N \times M \))
- \( R \): Simulated returns matrix (\( M \times N \))
- \( \Sigma \): Simulated standard deviations matrix (\( M \times N \))
- \( \alpha \): Coupling term coefficient

### Constraints
1. \( \sum_{i=1}^N W_{ij} = 1, \quad j = 1, 2, \ldots, M \)
2. \( W \geq 0 \)

---

## Decentralized Problem

### Expected Portfolio Return
For investor \( i \):
\[
R_i(W_i) = \sum_{j=1}^N W_{ij} \cdot \text{Expected Return of Asset } j
\]

### Portfolio Risk
\[
\sigma_i(W_i) = \sqrt{\sum_{j=1}^N \sum_{k=1}^N W_{ij} W_{ik} \cdot \text{Covariance}(j, k)}
\]

### Coupling Term
\[
| R_i(W_i) - \bar{R} | = \left| R_i(W_i) - \frac{1}{M} \sum_{j=1}^M R_j(W_j) \right|
\]

---

## Primal Decomposition Method

### Steps
1. **Decompose Global Objective**:
   \[
   J_\text{Global} = \sum_{i=1}^M J_i(W_i)
   \]
2. **Optimize Locally**:
   \[
   J_i(W_i) = -R_i(W_i) + \lambda \cdot \sigma_i(W_i) + \alpha \cdot |R_i(W_i) - \bar{R}|
   \]
3. **Update Global Variable**:
   \[
   \bar{R} = \frac{1}{M} \sum_{i=1}^M R_i(W_i)
   \]

---

## ADMM for Decentralized Portfolio Optimization

### Augmented Lagrangian Formulation
\[
L_\rho(W, Z, U) = \sum_{i=1}^M J_i(W_i) + \frac{\rho}{2} \sum_{i=1}^M \| W_i - Z + U_i \|^2
\]

Where:
- \( Z \): Consensus variable
- \( U \): Dual variable
- \( \rho \): Penalty parameter

### ADMM Steps
1. **Update \( W_i \)**:
   \[
   W_i^{k+1} = \arg\min_{W_i} \left( J_i(W_i) + \frac{\rho}{2} \| W_i - Z^k + U_i^k \|^2 \right)
   \]
2. **Update \( Z \)**:
   \[
   Z^{k+1} = \frac{1}{M} \sum_{i=1}^M (W_i^{k+1} + U_i^k)
   \]
3. **Update \( U_i \)**:
   \[
   U_i^{k+1} = U_i^k + (W_i^{k+1} - Z^{k+1})
   \]
4. **Convergence Check**:
   \[
   r^k = \frac{1}{M} \sum_{i=1}^M \| W_i^{k+1} - Z^{k+1} \|, \quad s^k = \rho \| Z^{k+1} - Z^k \|
   \]

---

## Fast ADMM

Fast ADMM introduces variable splitting:
\[
J_i(W_i, P_i) = J_i(W_i) + \frac{\rho}{2} \sum_{j=1}^N (P_{ij} - W_{ij} + Z_j - U_{ij})^2
\]

### Fast ADMM Steps
1. Update \( W_i \) and auxiliary variable \( P_i \):
   \[
   W_i^{k+1} = \arg\min_{W_i} J_i(W_i, P_i^k)
   \]
   \[
   P_i^{k+1} = \arg\min_{P_i} J_i(W_i^{k+1}, P_i)
   \]
2. Update \( Z \) and \( U \) as in standard ADMM.

---

## Results
- Convergence behavior and portfolio distributions are analyzed for various parameter settings (\( \rho, \alpha \)).
- The repository includes visualizations demonstrating convergence for up to 50 investors.
