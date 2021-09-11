
magnets=int(input())

position=[]
count=0
for i in range(magnets):
    temp_input=int(input())
    position.append(temp_input)
# print(position)

for i in range(1,len(position)):
    if position[i]==position[i-1]:
        continue
    else:
        count=count+1

print(count+1)