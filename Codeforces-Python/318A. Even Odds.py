
# Solved after 7 Wrong answer & Time limit exceeded  (^_^)

number, position = map(int, input().split())

partition=0

if  number%2==0:
	partition=number/2
else:
	partition=int(number/2+.5)


if partition>=position:
	print(int(position*2-1))
else:
	print(int((position-partition)*2))






############ Time limit exceeded ############ 

# number, position = map(int, input().split())
# even=[]
# odd=[]
# for i in range(1,number+1):
# 	if i%2==0:
# 		even.append(i)
# 	else:
# 		odd.append(i)
# odd_even_list=odd+even
# print(odd_even_list[position-1])


################

# print(partition)

# elif  number%2==0 and (number/2)<position:
# 	print(int((position- (number/2))*2))


# elif  number%2!=0 and (number/2)>=position:
# 	print(position*2-1)

# elif  number%2!=0 and (number/2)<position:
# 	print(int((position-number/2)*2-1))
