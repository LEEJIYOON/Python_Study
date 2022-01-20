from collections import deque
from itertools import combinations
from copy import deepcopy

n,m=map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

# n,m=5,3
# graph=[[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]



home=deque()
chicken=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            home.append((i,j))
        elif graph[i][j]==2:
            chicken.append((i,j))
            
min_distance=987654321

survive_store=deque(combinations(chicken,m))



distance=0
answer=0
chicken_distance=987654321

while survive_store:
    i=survive_store.popleft()
    home_distance=deepcopy(home)
    answer=0
    while home_distance:
        now=home_distance.popleft()
        min_distance=987654321
        for j in range(m):
            dx=abs(i[j][0]-now[0])
            dy=abs(i[j][1]-now[1])
            distance=(dx+dy)
            min_distance=min(min_distance,distance)
        answer+=min_distance
    chicken_distance=min(answer,chicken_distance)


print(chicken_distance)
            
        
