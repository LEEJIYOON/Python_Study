INF=int(1e9)

n=int(input())  #number of node
m=int(input())  #number of line

graph=[[INF] *(n+1) for _ in range(n+1)]

for i in range(n+1):
  graph[i][i]=0

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=c
  

  
  
for k in range(1,n+1):   #1부터 시작
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
