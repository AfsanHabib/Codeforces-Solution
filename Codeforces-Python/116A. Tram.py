
# Solved

tram_stops = int(input())

i = int(0)

#empty arry
exits_enter_Array = []


while i<tram_stops:
    # Taking input as a list
    input_array = list(map(int, input().split()))
    # Store input list in the empty array
    exits_enter_Array.append(input_array)
    i = i+1

capacity = 0
count = 0

# loop by list
for j in exits_enter_Array:
    count = count - j[0] + j[1]
    if capacity < count:
        capacity = count

print(capacity)


