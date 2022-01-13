from collections import deque

N,M,K,X=map(int, input().split())

city_distance=[-1]*(N+1)
city_distance[X]=0

graph=[[] for _  in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)



q=deque([X])

while q:
    now=q.popleft()

    for next in graph[now]:
        if city_distance[next]==-1:
            city_distance[next]=city_distance[now]+1
            q.append(next)

check=False

for i in range(N+1):
    if city_distance[i]==K:
        print(i)
        check=True


if check==False:
    print(-1)
