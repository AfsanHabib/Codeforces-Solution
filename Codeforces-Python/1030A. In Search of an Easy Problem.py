

people= int(input())
thinks_list=list(map(int,input().split()))

easy=0

for i in thinks_list:
	if i == 1:
		print("HARD")
		break
	else:
		easy+=1


if easy==len(thinks_list):
	print("EASY")
