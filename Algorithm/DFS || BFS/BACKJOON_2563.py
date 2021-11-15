from collections import deque
from copy import deepcopy


n,m=map(int,input().split())

graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

ice=[[0]*m for _ in range(n)]

queue=deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]>0:
            queue.append((i,j))


def bfs(x,y):
    q=deque()
    q.append((x,y))

    visit=[[0]*m for _ in range(n)]
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<nx<n and 0<ny<m and visit[nx][ny]==0 and island[nx][ny]!=0:
                visit[nx][ny]=1
                island[nx][ny]=0
                q.append((nx,ny))


melt=0
time=0

while queue:
    time+=1
    k=len(queue)

    for _ in range(k):
        x,y=queue.popleft()
        melt=0
    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if graph[nx][ny]==0 and ice[nx][ny]<time:
                melt+=1
        
            
        if graph[x][y]-melt>0:
            graph[x][y]-=melt
            queue.append((x,y))
        else:
            graph[x][y]=0
            ice[x][y]=time
    

    island=deepcopy(graph)
    count=0
    for i in range(n):
        for j in range(m):
            if island[i][j]!=0:
                bfs(i,j)
                count+=1
    
    if count >=2:
        print(time)
        break


if count<2:
    print(0)
