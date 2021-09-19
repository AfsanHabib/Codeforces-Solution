
# Solved

# In Python, there are two types of division operators:

# Divides the number on its left by the number on its right and returns a floating point value.
# Ex:5/2=2.5

# Divides the number on its left by the number on its right, rounds down the answer, and returns a whole number.
# Ex:5//2=2


groups=input()
group_members=list(map(int, input().split()))

one=0
two=0
three=0
four=0
ride=0

# group_members.sort(reverse=True)

for i in group_members:
    if i == 1:
        one+=1
    if i == 2:
        two+=1
    if i == 3:
        three+=1
    if i == 4:
        four+=1

# print(one, two, three, four)

ride=four

while one!=0 and three!=0:
    three=three-1
    one=one-1
    ride=ride+1

if one==0 and three!=0:
    ride=ride+three
    three=0

ride=ride+two//2

if two%2!=0:
    if one<=2:
        ride=ride+1
        two=0
        one=0
    else:
        one=one-2
        ride=ride+1
        two=0

if one!=0:
    ride=ride+one//4
    if one%4!=0:
        ride=ride+1



print(ride)

# while one!=0 and three!=0:
#     ride+=1
#     one-=1
#     three-=1

# if one == 0 and three!=0:
#     ride=ride+three
#     three=0

# ride=ride+two/2

# if two%2 != 0:
#     if one <= 2:
#         ride=ride+1
#         one =0
#         two =0
#     else:
#         ride=ride+1
#         one-=2
#         two-=0

#     if one !=0:
#         ride=ride+one/4

#         if one%4!=0:
#             ride=ride+1

# print(int(ride))

