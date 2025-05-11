# Knapsack Problem Solver

## Problem Statement

In this exercise, you will design various algorithms to solve the well-known **Knapsack problem**. You are given a knapsack with limited capacity and a collection of items, each with a specific weight and value. Your objective is to **maximize the total value** of the items packed into the knapsack, without exceeding its total capacity.

---

## Data Format

Each problem instance is represented by a text file, structured line by line. The total number of lines is **n + 1**, where **n** is the number of available items.

- The **first line** contains two integers:  
  - the **total capacity of the knapsack**, and  
  - the **number of items**.

- Each of the **following n lines** contains a pair of integers:  
  - the **weight** and  
  - the **value** of an item.

---

## Grading Criteria

Your submission will be evaluated based on the following:

- **a)** The quality of the final solutions (how optimal they are).  
- **b)** The execution time of your algorithms.  
- **c)** The correctness of your implementation.

---

## Programming Techniques

The following algorithmic approaches are implemented:

- **a) Random**:  
  Random selection of items until the knapsack is full.

- **b) Greedy**:  
  Greedy heuristic based on the **value-to-weight ratio**.

- **c) DP (Dynamic Programming)**:  
  Solves the problem using a bottom-up **dynamic programming** approach.

- **d) B&B (DFS)**:  
  **Branch and Bound** technique using **Depth First Search** strategy.

- **e) B&B (BFS)**:  
  **Branch and Bound** technique using **Best First Search** strategy.

- **f) (Bonus) B&B (LDS)**:  
  **Branch and Bound** using **Limited Discrepancy Search**—a variant that explores decisions deviating from a greedy heuristic up to a limited discrepancy level.

---

## Output Files

The solution files have this format:

- `pr1.csv` 
- `pr2.csv`  
- `pr3.csv`  
- `pr4.csv`  
- `pr5.csv`  
- `pr6.csv`  

Each file contains **one line** which is a list of **0s and 1s**, separated by commas, representing the item selection for one instance:

- `1` means the item is **selected**.  
- `0` means the item is **not selected**.

**Important:**  
The **order of items in the output must exactly match** the original order in the input file.

---