

test_case=int(input())

while test_case>0:
	a,b,c=map(int,input().split())

	test_case-=1

	if a>b and a>c:
		print("0",end=' ')
	else:
		print(max(b,c)+1-a,end=' ')

	if b>a and b>c:
		print("0",end=' ')
	else:
		print(max(a,c)+1-b,end=' ')

	if c>b and c>a:
		print("0",end='\n')
	else:
		print(max(a,b)+1-c,end='\n')
	