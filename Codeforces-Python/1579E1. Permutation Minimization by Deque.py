
from collections import deque

test_case = int(input())

for i in range(test_case):
    permutation_size = int(input())
    elements=  list(map(int,input().split()))
    first_element = deque([elements[0]])

    for j in elements[1:]:
        if j <= first_element[0]:
            first_element.appendleft(j)
        elif j >= first_element[-1]:
            first_element.append(j)
        else:
            first_element.append(j)

    print(*first_element)