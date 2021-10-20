# solved

name1= str(input())
name2= str(input())
pile= sorted(str(input()))


add_name=sorted(name1+name2)

if add_name==pile:
	print("YES")
else:
	print("NO")