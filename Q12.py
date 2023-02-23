import numpy as np
S=np.array([[1,-1,1],[1,0,1],[1,1,2]])
def gram_schmidt(S):
    Q=[]
    for i in range(S.shape[0]):
        u=S[i]
        for j in range(len(Q)):
            u=u-np.dot(S[i],Q[j])*Q[j]
        Q.append(u/np.linalg.norm(u))
    return np.array(Q)
Q=gram_schmidt(S)
print("orthonormal basis:")
print(Q)