# Solved

children_in_queue, time = map(int,input().split())

queue = input()

while time:
    queue=queue.replace('BG','GB')
    time=time-1
print(queue)


