#Solved

rooms = int(input())
count=0
while rooms:
    people_in_room,rooms_capacity=map(int, input().split())
    if rooms_capacity-people_in_room>=2:
        count=count+1
    rooms = rooms-1
print(count)