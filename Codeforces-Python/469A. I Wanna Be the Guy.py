# Solved

n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

p.pop(0)
q.pop(0)

new_list=p+q
new_list.sort()
set_new_list=set(new_list)

if len(set_new_list)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

# for i in set_new_list:
#     if i==n:
#         print("I become the guy.")
#         break
#     elif i>n:
#         print("I become the guy.")
#         break
#     else:
#         print("Oh, my keyboard!")
#         break




    




 