test_case=int(input())

for i in range(test_case):
	n = int(7)
	lst = list(map(int,input().strip().split()))[:n]

	lst.sort()

	print( lst[0],lst[1],lst[6]-(lst[0]+lst[1]))
