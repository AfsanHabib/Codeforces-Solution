for i in range(int(input())):
	s=input()

	s_len=len(s)

	s_half_len=int(s_len/2)

	if s_len%2!=0:
		print("NO")
	else:
		new_s=list(map(''.join, zip(*[iter(s)]*s_half_len)))

		if new_s[0]==new_s[1]:
			print("YES")
		else:
			print("NO")