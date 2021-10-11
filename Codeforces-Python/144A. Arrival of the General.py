
soldiers=int(input())
height=list(map(int,input().split()))


max_height=max(height)
min_height=min(height)

max_height_index =height.index(max_height)
height.reverse()
min_height_index =height.index(min_height)
# min_height_index =height[::-1].index(min_height)


if min_height_index+max_height_index+2>soldiers:
    print(max_height_index+min_height_index-1)
else:
    print(min_height_index+max_height_index)





# soldiers=int(input())
# height=list(map(int,input().split()))

 
# max_height=max(height)
# min_height=min(height)

# max_height_index =height.index(max_height)
# min_height_index =height[::-1].index(min_height)


# print(min_height_index)

# if min_height_index+max_height_index+2>soldiers:
#     print(max_height_index+min_height_index-1)
# else:
#     print(min_height_index+max_height_index)








# soldiers=int(input()) 
# height=list(map(int,input().split()))

# height.reverse()

# print(height)
 
# max_height=height[0]
# min_height=height[0]
 
 
# for i in range(0,len(height),1):
#   max_height=max(max_height,height[i])
#   min_height=min(min_height,height[i])
 
# max_height_index=height.index(max_height)
# min_height_index=height.index(min_height)
 
# if min_height_index<max_height_index:
#   min_height_index+=2
 
# ans=max_height_index+(soldiers-1)-min_height_index
 
# print(ans)
 
 





# n=int(input())
# a=list(map(int,input().split()))
# b = a[:]
# b.reverse()
# u = a.index(max(a))
# l = n-1-b.index(min(a))


# print(b)
# print(u)

# print(l)


# if u > l:
#   print(u+(n-1-l)-1)
# else:
#   print(u+(n-1-l))


# soldiers=int(input()) 
# height=list(map(int,input().split()))
# reverse_height = height[:]



# max_height=max(height)
# max_height_index=height.index(max_height)
# # max_height_index=height.index(max(height))
 
# min_height=min(height)
# min_height_index=height.index(min_height)
# # min_height_index=height.index(min(height))
 
# if min_height_index<1:
# 	min_height_index+=1
 
# if min_height_index<max_height_index:
# 	min_height_index+=1
 
# ans=max_height_index+(soldiers-1)-min_height_index
 
# print(ans)























# soldiers=int(input()) 
# height=list(map(int,input().split()))

# max_height=int(0)
# min_height=int(101)


# for i in range(0,len(height),1):
# 	if i>max_height:
# 		max_height=height[i]
# 		max_height_index=[i]
# 	if i<=min_height:
# 		min_height=height[i]
# 		min_height_index=i

# if max_height_index>min_height_index:
# 	min_height_index+=1

# ans=max_height_index+(soldiers-1)-min_height_index

# print(ans )











# soldiers=int(input()) 
# height=list(map(int,input().split()))

# max_height=max(height)
# max_height_index=height.index(max_height)
# # max_height_index=height.index(max(height))

# min_height=min(height)
# min_height_index=height.index(min_height)
# # min_height_index=height.index(min(height))

# if min_height_index<1:
# 	min_height_index+=1

# if min_height_index<max_height_index:
# 	min_height_index+=1

# ans=max_height_index+(soldiers-1)-min_height_index

# print(ans)



############################################

# soldiers=int(input()) 
# height=list(map(int,input().split()))

# # max_height=max(height)
# # max_height_index=max(height.index())

# max_height_index=height.index(max(height))

# min_height_index=height.index(min(height))

# # min_height=min(height)
# # min_height_index=
# list_lenght=len(height)-1

# if min_height_index<max_height_index:
# 	min_height_index+=1

# ans=max_height_index+(soldiers-1)-min_height_index

# print(ans)