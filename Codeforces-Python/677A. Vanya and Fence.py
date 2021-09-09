# Solved

friends,fence_height = map(int,input().split())
person_height=list(map(int,input().split()))

count=0

for i in person_height:
    if i>fence_height:
        count=count+2
    else:
        count=count+1

print(count)