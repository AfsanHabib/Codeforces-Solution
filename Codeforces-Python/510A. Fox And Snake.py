# Solved
#############

row, col = map(int,input().split())

lst=[]

for i in range(row):
	if i%2!=0:
		string1=(((".")*(col-1))+"#")
		lst.append(string1)
	else:
		string2=("#"*col)
		lst.append(string2)

for k in range(3,len(lst),4):
	lst[k]=''.join(reversed(lst[k]))

for ans in lst:
	print(ans)





"""
row, col = map(int,input().split())
lst=[]


for i in range(row):
	if i%2!=0:
		# print(col-1* str(".")+str("#"))
		string1=(((".")*(col-1))+"#")
		lst.append(string1)
	else:
		# print(col*str("#"))
		string2=("#"*col)
		lst.append(string2)


for k in range(3,len(lst),4):
	lst[k]=''.join(reversed(lst[k]))
	# lst[k]=reversed(lst[k])


for ans in lst:
	print(ans)
# print(lst)


# # ans_lst=lst[:3]
# ans_lst=[] 
# # for j in lst:



# for k in range(3,len(lst),2):
# 	ans_lst.append(  ''.join(reversed(lst[k])) )
# 	# print(lst[k])

# # print(lst)
# print(ans_lst)
"""