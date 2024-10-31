from calc_SVD import calc_SVD
import numpy as np



def spring_mass(n_springs, Cs, Ms, fixed_ends):
    #Checking to make sure the inputed parameters agree with each other
    if n_springs>len(Ms)+1 or n_springs<len(Ms):
        print(f"\nThe inputed system has an incompatible number of springs,{n_springs}, vs. masses, {len(Ms)}.\n")
        return()
    if n_springs!=len(Cs):
        print("\nError: The length of your spring constant matrix should be the same as the number of springs in the system.\n")
        return()
    if fixed_ends==0:
        print("\nError: A free-free system results in an unstable solution. Apply either one or two fixed ends.\n")
        return()
    C=np.diag(Cs)
    #making K
    K = np.zeros([len(Ms), len(Ms)])

    for i in range(len(Ms)-1):
        K[i,i]=Cs[i]+Cs[i+1]
        if i<len(Ms):
            K[i,i+1]=-Cs[i+1]
            K[i+1,i]=-Cs[i+1]
    #if fixed_free, we need to set the Boundary condition at the free end
    if fixed_ends==1:
        K[-1,-1]=Cs[-1]
    else:
        K[-1,-1]=Cs[-1]+Cs[-2]

    print(f"\nK matrix for the inputed system: \n{K}\n")

    
#Taken from the link the professor gave us for calculating the psuedoinverse

    U, s, VT, cond_num, A_inv = calc_SVD(K)
    print(f"condition number: {cond_num}\n")

    # reciprocals of s
    s=np.diag(s)
    d = 1.0 / s
    # create m x n D matrix
    D = np.zeros(K.shape)
    # populate D with n x n diagonal matrix
    D[:K.shape[1], :K.shape[1]] = np.diag(d)
    # calculate pseudoinverse
    B = VT.T.dot(D.T).dot(U.T)
    #defining forces and solving for dispalcements
    f=-9.81*np.array(Ms)
    #f=np.array(Ms) for calculating without g
    u = B @ f
    u_no_zeros=u
    u = np.insert(u, 0, 0) 
    
    if fixed_ends==2:
        u= np.append(u, 0)
        #Now we have zero values at fixed ends and our u is the right size

    elongations=np.zeros(n_springs)
    stresses=np.zeros(n_springs)
    if fixed_ends>0:
        elongations[0]=u[1]
    for i in range(n_springs):
        elongations[i]=u[i+1]-u[i]
    internal_forces=(Cs)*elongations
    return(u_no_zeros, elongations, internal_forces)

while True:
    Cs=[]
    Ms=[]

    n_masses=int(input("Please input the number of masses for the system: "))
    fixed_ends=int(input("Please input the number of fixed ends (1 or 2 for a stable system): "))
    if fixed_ends==0:
        print("\nError: A free-free system results in an unstable solution. Apply either one or two fixed ends.\n")
        pass
    elif fixed_ends==1:
        n_springs=n_masses
    elif fixed_ends==2:
        n_springs=n_masses+1
    else:
        print("error: The number of fixed ends should be either 1 or 2")
        pass
    for i in range(n_springs):
        c=int(input(f"Please input a spring constant for spring {i+1}: "))
        Cs.append(c)
    for i in range(n_masses):
        m=int(input(f"Please input a value for mass {i+1}: "))
        Ms.append(m)
        
    #calling function with correct parameters:   
    [u,e,s]=spring_mass(n_springs, Cs, Ms, fixed_ends)
    print(f"u:\n{u}\n\ne:\n{e}\n\nw:\n{s}\n\n")

    end_code=input("Type q to end the program. Type any other input to start again. ")
    if end_code=="q":
        break

