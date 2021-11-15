from collections import deque

n = int(input())
m=int(input())

#시작 node가 1이기때문
graph=[[i] for i in range(n+1)]

#각각의 간선을 종합
for _ in range(m):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

virus=[False]*(n+1)


def bfs(graph,v,virus):

    if len(graph[1])==1:
        return 0
    queue=deque([v])
    virus[v]=True
    result=0

    while queue:
        v=queue.popleft()

        for i in graph[v]:
            if not virus[i]:
                queue.append(i)
                virus[i]=True
                result += 1
    
    return result

print(bfs(graph,1,virus))
