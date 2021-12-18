




for i in range(int(input())):
	x=input()
	ce=x.count('E')
	cn=x.count('N')


	if cn>1 or cn==0:
		print("YES")
	else:
		print("NO")





# for i in range(int(input())):

# 	s= input()

# 	E=0
# 	N=0

# 	set1 = set(s)
# 	len_s=len(s)


# 	for i in s:
# 		if i == 'E':
# 			E = E + 1


# 	for j in s:
# 		if j == 'N':
# 			N = N + 1


# 	if len(set1)==1:
# 		print("YES")


# 	elif s[0]=='E' and s[-1]=='E' and E==len_s-3:
# 		print("YES")


# 	elif s[0]=='N' and s[-1]=='N' and N==len_s-1:
# 		print("YES")

# 	else:
# 		print("NO")




  










# for i in range(int(input())):

# 	s= input()

# 	set1 = set(s)



# 	if len(set1)==1:
# 		print("YES")
# 	elif (s[0]=='E' and s[-1]=='E') or  (s[0]=='N' and s[-1]=='N') :
# 		print("YES")
# 	else:
# 		print("NO")