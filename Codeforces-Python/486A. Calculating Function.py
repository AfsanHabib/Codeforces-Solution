# Solved

positive_integer = int(input())

odd=0

if positive_integer%2==0:
	print(int(positive_integer/2))
else:
	odd=(positive_integer/2)+1
	print(int(-odd))


############ Time limit exceeded ############ 
# positive_integer = int(input())
# even=[]
# odd=[]
# for i in range(1,positive_integer+1):
# 	if i%2==0:
# 		even.append(i)
# 	else:
# 		odd.append(i)
# print(sum(even)- sum(odd))
#############################################