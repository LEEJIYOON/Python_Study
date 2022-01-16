#Snake
from collections import deque

n=int(input()) # board size
k=int(input()) #apple size

apple_loc=[]


graph=[[0]*n for _ in range(n)]

for _ in range(k):
    a,b=map(int,input().split())
    apple_loc.append((a-1,b-1))

graph[0][0]=-1

for i in apple_loc:
    graph[i[0]][i[1]]=1


l=int(input())
move_status=[]

for _ in range(l):
    a,b=input().split()
    move_status.append((int(a),b))



def new_direction(direction,command):
    if direction =="right" and command=="L":
        return "up"
    elif direction =="right" and command=="D":
        return "down"
    elif direction =="left" and command=="L":
        return "down"
    elif direction =="left" and command=="D":
        return "up"
    elif direction =="up" and command=="L":
        return "left"
    elif direction =="up" and command=="D":
        return "right"
    elif direction =="down" and command=="L":
        return "right"
    elif direction =="down" and command=="D":
        return "left"



def moving(direction,x,y):
    if direction=="right":
        return x,y+1
    if direction=="up":
        return x-1,y
    if direction=="down":
        return x+1,y
    else:
        return x,y-1


time=0
direction="right"
snake=deque([(0,0)])
x,y=0,0 #head position

keep_going="go"

for i in move_status:
    temp_time=0
    move_count=i[0]-time
    command=i[1]
    while temp_time < move_count :
        time+=1
        temp_time+=1
        x,y=moving(direction,x,y)
        if x>=n or x<0 or y>=n or y<0:
            keep_going="stop"
            break
        if graph[x][y]==-1:
            keep_going="stop"
            break
        if graph[x][y]==0:
            graph[x][y]=-1
            snake.append((x,y))
            i,j=snake.popleft()
            graph[i][j]=0
        if graph[x][y]==1:
            graph[x][y]=-1
            snake.append((x,y))
    if keep_going=="go":
        direction=new_direction(direction,command)
    else:
        break ########### break twice###################

if keep_going=="stop":
    print(time)
else:
    while keep_going=="go":
        time+=1
        x,y=moving(direction,x,y)
        if x>=n or x<0 or y>=n or y<0:
            break
        if graph[x][y]==-1:
            break
    print(time)
