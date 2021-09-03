
#Solved

num, k = map(int, input().split())
i = int(0)
for i in range (i,k):
    if(num%10>0):
        num = num -1
    else:
        num = num/10
print(int(num))
