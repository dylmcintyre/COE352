# COE352 - Project 1

For this project, I created two Python files:

--calc_SVD.py: Defines a function calc_SVD which takes an A matrix as input and returns (U,S,V, k, A_inv)
where:

      -U, S, and V are the matrices from SVD decomposition
      -k is the condition number of the inputted matrix
      -A_inv is the inverse of the inputed matrix
      
First the user defined function results are printed, then the black box calculations from the numpy svd function are printed.
Part 1 response:
      For part 1, the black box calculations and self-implemented calculations of U, S, and V resulted in identical values although sometimes values in the V matrix differed in sign. Overall, when comparing the resulting inverses of A computed from the SVD matrices, there were slight differences, however both inverses were comparable. The calc_SVD funciton was used successfully to solve the spring mass system by decomposing the K matrix, showing that the calc_SVD function successfully calculates inverse(A).

--spring_mass.py: Allows the user to input the number of masses and fixed ends for a Spring-Mass system. Then the user can input spring constant and mass values for the system.
Based on user input, the program will output the K matrix and condition number for the system as well as the computed displacement, elongation, and internal force values of the system.

For a free-free system with 0 fixed_ends:
For a free-free system where neither end of the system are constrained, we do not get a stable answer.
For a this type of system, we cannot set u_0 and u_final equal to zero, so we end up with 1 less elongation equation than unknown displacements. Because we end up with less equations than unknowns, the system is not correctly constrained and we cannot get an answer. For the free-free system, our K-matrix does not have full rank and is thus not invertible. If we try and perform SVD decomp on the K matrix for a free-free system, the elements of the inverse blow up towards infinity.

