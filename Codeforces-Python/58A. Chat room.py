#Solved

str = input()

hello = "hello"
j=0

ans=0

i=0

for i in str:
    if i == hello[j]:
        j = j+1
        ans = ans+1
    if ans==5:
        break

if(ans==5):
    print("YES")
else:
    print("NO")

