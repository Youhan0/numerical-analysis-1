'''算法A'''
import numpy as np
N=9
I=np.zeros((N+1,1))
I[0]=0.6321
for n in range(N):
    I[n+1]=1-(n+1)*I[n]

print(I)
print("I_9=",I[9])

