import heapq #탐색을 최소화하기 위해, heapq을 사용


n,m=map(int,input().split()) #n은 node 갯수, m은 간선 갯수
start=int(input()) #시작점

INF=int(1e9)
graph=[[] for i range(n+1)] #node 넘버와 graph 행 맞추기위해 n+1
distance=[INF]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  
  
def dijkstra(start):
  h=[] #heapq은 앞에가 거리, 뒤에가 노드
  distance[start]=0
  heapq.heappush(h,(distance[start],start))
  while h:
    dist,now=heapq.heappop(h)
    
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost=dist+i[1]
      if distance[i[0]] > cost: # graph는 앞에가 node 뒤에가 거리
        distance[i[0]]=cost
        heapq.heappush(q,cost,i[0])
