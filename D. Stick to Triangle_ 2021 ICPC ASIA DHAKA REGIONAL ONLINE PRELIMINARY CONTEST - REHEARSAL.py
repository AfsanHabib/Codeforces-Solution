

#___________Afsan Habib___________#

import itertools

#___________Start Input Functions___________#

def int_num_input():
    return (int(input()))
 
def int_list_input():
    return (list(map(int,input().split())))
 
def insr_input():
    s = input()
    return (list(s[:len(s) - 1]))
 
def invr_input():
    return(map(int,input().split()))
 
#___________End Input Functions___________



#___________Start Solve Functions___________#


def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]



def solve():

	t=int(input())

	
	while t:
		n=int(input())
		lst=[]

		for p in partitions(n, 3):
			if 0 in p:
				pass
			else:
				lst.append(sorted(p))

		unique = [list(i) for i in set(tuple(i) for i in lst)]

		count=0

		for i in unique:
			if max(i)>n//2:
				count=count+1


		print(len(unique)-count)
		# print(unique)


		t=t-1

#___________End Solve Functions___________
 

#___________Start Main Functions___________#
def main():
	solve()
	return
 
if __name__ == "__main__":
    main()
#___________End Main Functions___________
