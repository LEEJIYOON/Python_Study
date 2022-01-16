from itertools import combinations
from collections import deque
from copy import deepcopy

n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

virus=deque()
possible_wall=deque()


for i in range(n):
    for j in range(m):
        if graph[i][j]!=0:
            if graph[i][j]==2:
                virus.append((i,j))
        else:
            possible_wall.append((i,j))

position_graph=deepcopy(graph)


dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(virus):
    count=0
    while virus:
        x,y=virus.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<n and nx>=0 and ny<m and ny>=0 and position_graph[nx][ny]==0:
                position_graph[nx][ny]=2
                virus.append((nx,ny))
    for a in range(n):
        for b in range(m):
            if position_graph[a][b]==0:
                count+=1
    return count



max_area=0
iter_position=list(combinations(possible_wall,3))


for i in iter_position:
    position_graph=deepcopy(graph)
    virus_copy=deepcopy(virus)

    for j in range(3):
        position_graph[i[j][0]][i[j][1]]=1
    
    trial=bfs(virus_copy)
    max_area=max(trial,max_area)


print(max_area)
