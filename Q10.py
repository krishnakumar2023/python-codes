import numpy as np
v1=np.array([1,-1,1])
v2=np.array([1,0,1])
v3=np.array([1,1,2])

u1=v1/np.linalg.norm(v1)
u2=v2-np.dot(v2,u1)*u1
u2=u2/np.linalg.norm(u2)
u3=v3-np.dot(v3,u1)*u1-np.dot(v3,u2)*u2
u3=u3/np.linalg.norm(u3)

print("orthonormal basis vectors:")
print(u1)
print(u2)
print(u3)