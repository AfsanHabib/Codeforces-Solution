# Solved

import math

mod=10**9+7
lst=[1]
ans=1

for i in range(1,2*(10**5)+1):
    lst.append((ans*i//2)%mod)
    ans=(ans*i)%mod
    
for j in range(int(input())):
    n=int(input())
    print(lst[2*n])