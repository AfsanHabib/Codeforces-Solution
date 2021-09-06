#Solved

played=int(input())
str = input()

Anton=0
Danik=0

for i in str:
    if i == 'A':
        Anton=Anton+1
    else:
        Danik=Danik+1

if Anton>Danik:
    print("Anton")
elif Danik>Anton:
    print("Danik")
else:
    print("Friendship")


