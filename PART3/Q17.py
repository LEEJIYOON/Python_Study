from collections import deque

n,k=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

s,ax,ay=map(int,input().split())


virus=deque()

for i in range(1,k+1):
    for a in range(n):
        for b in range(n):
            if graph[a][b]==i:
                virus.append((a,b,i))

time=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

while time <s:
    time+=1
    trial=len(virus)
    for i in range(trial):
        x,y,value=virus.popleft()
        
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]==0:
                graph[nx][ny]=value
                virus.append((nx,ny,value))
            

print(graph[ax-1][ay-1])
