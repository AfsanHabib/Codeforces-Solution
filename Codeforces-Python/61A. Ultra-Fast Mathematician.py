#Solved

number1 = input()
number2 = input()

j=0
answer = list()  

for i in number1:
	if i == number2[j]:
		# print("0")
		answer.append(0)
	else:
		# print("1")
		answer.append(1)
	j=j+1

for l in answer:
    print(l, end="")



# number1 = list(map(int,input()))
# number2 = list(map(int,input()))

# answer=[]

# for i in number1:
# 	for j in number2:
# 		if i == j:
# 			answer.append(0)
# 		else:
# 			answer.append(1)
# print(answer)


