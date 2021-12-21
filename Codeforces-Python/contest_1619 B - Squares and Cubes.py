

for i in range(int(input())):
	n=int(input())

	count=[0]

	if n==1:
		print(1)
	else:
		for i in range(1,n):

			if i*i>n:
				break

			if i*i<=n:
				count.append(i*i)
			if i*i*i<=n:
				count.append(i*i*i)
			else:
				pass

		print(len(set(count))-1)

