# Solved

number=list(map(int,input()))

ans=0

for i in number:
    if i==4 or i==7:
        ans=ans+1

if ans == 4 or ans ==7:
    print("YES")
else:
    print("NO")







