'''算法B'''
N=14
IB=np.zeros((N+1,1))
IB[N]=1/(N+1)
for n in range(N,0,-1):
    IB[n-1]=(1-IB[n])/(n)
#for n in range(N):
#    IB[13-n]=(1-IB[14-n])/(14-n)

print(IB)
print("IB_9=",IB[9])


