# COE352 - Project 1: Singular Value Decomposition and Spring-Mass System Analysis

This project consists of two Python files:
---

### calc_SVD.py

This file defines the `calc_SVD` function, which takes a matrix \( A \) as input and returns several key values:

- **`U`**, **`S`**, and **`V.T`** matrices from the SVD decomposition
- **`k`**: The condition number of the inputted matrix \( A \)
- **`A_inv`**: The calculated inverse of matrix \( A \)

The function has a main which defines an A matrix and compares it to the Black Box response. The user can also simply call the calc_SVD function to get SVD results.

**Part 1 Response**:  
- The black-box and self-implemented calculations of \( U \), \( S \), and \( V \) yielded identical values, although there were occasional sign differences in the \( V \) and \( U \) matrices.
- Comparing the inverses of \( A \) computed from the SVD matrices showed slight differences, but both were comparable. When I multiplied A by inverse(A) computed from the function, I got the identity matrix, verifying that the returned inverse works. The `calc_SVD` function successfully decomposed the \( K \) matrix in the spring-mass system which gave us viable results, demonstrating that it calculates `inverse(A)` effectively.

---

### spring_mass.py

This file simulates a Spring-Mass System based on user input. The user can define:

- The number of masses
- The number of fixed ends of the system
- Spring constant and mass values

The program then calculates and outputs:

- **`K` matrix**: Stiffness matrix for the system
- **Condition number** of the system
- **Displacement**, **elongation**, and **internal forces** for each mass in the system

**Part 2 Response**:
In a free-free system (where neither end is constrained):
- We end up with fewer elongation equations than unknown displacements, so the system does not have a unique solution.
- The \( K \) matrix lacks full rank and is not invertible.
- Attempting SVD decomposition on the \( K \) matrix results in elements of the inverse tending toward infinity, showing the system isn't stable.

---

