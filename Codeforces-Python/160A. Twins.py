# Solved

coins=int(input())
values=list(map(int,input().split()))

sotr_values=sorted(values)
sum1=sum(values)/2
sum2=0
ans=0


# Backwards for loop 
for i in reversed(sotr_values):
    sum2=sum2+i
    ans=ans+1
    if sum2>sum1:
        break

print(ans)
