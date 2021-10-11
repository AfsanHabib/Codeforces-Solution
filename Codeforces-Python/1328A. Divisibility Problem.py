# Solved

test_case=int(input())
ans=int(0)

while test_case>0:
	a,b=map(int,input().split())
	
	rem=a%b
	# div=a//b
	# new_b=b-rem
	# new_a=rem+div+b

	if a%b==0:
		print("0")
	elif a<b:
		print(b-a)
	else:
		print(b-rem)

	test_case-=1
