# Solved

test_case=int(input())

for i in range(test_case):
	weapons,health=map(int,input().split())
	arr = sorted(map(int, input().split()),reverse=True)
	
	# input_string = input()
	# list  = input_string.split()
	first_value = arr[0]
	second_value = arr[1]
	total_value = first_value+second_value
	ans = health//total_value * 2
	rem = health%total_value
	if rem == 0:
		ans += 0
	elif rem <= first_value:
		ans += 1
	else:
		ans += 2
	print(ans)	

