import numpy as np
import sklearn.preprocessing

def calc_SVD(A):
    if not isinstance(A, np.ndarray) or not A.ndim == 2:
        print("\n\nERROR: A is not a two dimensional numpy array\n\n")
        return()
  
    AAt=A @ A.T
    AtA= A.T @ A
    if np.linalg.det(AAt)==0:
        print("\n\nERROR: Matrix A is not invertible.\n\n")
        return(0)  
    e_vals_U, e_vecs_U=np.linalg.eig(AAt)
    s_indices=np.argsort(e_vals_U)[::-1]
    e_vecs_U=e_vecs_U.T[s_indices]
    e_vals_U=e_vals_U[s_indices]

    S=np.zeros_like(A)
    S_inv=np.zeros_like(A.T)

    S=np.diag(np.sqrt(e_vals_U))
    S_inv=np.diag(1/np.sqrt(e_vals_U))

    e_vals_V, e_vecs_V = np.linalg.eig(AtA)
    s_indices=np.argsort(e_vals_V)[::-1]
    e_vecs_V=e_vecs_V.T[s_indices]

    V=e_vecs_V.T #Note e vectors are already normalized by l2 norm
    U=e_vecs_U.T

    k=abs(np.sqrt(max(e_vals_U)/min(e_vals_U)))
    #print(f"Condition Number: {k}")
    A_inv=V@S_inv@U.T
    return(U,S,V.T, k, A_inv)
def main():
    #For the main, I put an A function to test my code. In order to test the calc_SVD function, just call it with the A matrix of your choice.
    
    A=[[1, 1, 3],
    [1, -1, 7],
    [0, 2, 5]]

    A=np.array(A)

    [U,S,Vh, cond_num, A_inv]=calc_SVD(A)
    print(f"\n--------------MY SVD RESULTS:-------------\n")
    print(f"U:\n{U}\nS:\n{S}\nV:\n{Vh}\n\nCond Num: {cond_num}")
    print(f"\nInverse of A:\n{A_inv}\n")

    #Using black box calculation
    [U,S,Vh]=np.linalg.svd(A)
    print(f"\n----------BLACK BOX CALCULATIONS:----------\n")
    print(f"U:\n{U}\nS:\n{np.diag(S)}\nV:\n{Vh}\n")
    return()

if __name__  == "__main__":
    main()
