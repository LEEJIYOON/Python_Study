from collections import deque

def solution(N, stages):
    
    state=[[0,0] for i in range(N+1)]
    fail_rate=[[0,i] for i in range(N+1)]
    
    for i in stages:
        if i==N+1:
            for j in range(1,N+1):
                state[j][1]+=1
        else:
            state[i][0]+=1
            for k in range(1,i+1):
                state[k][1]+=1
    
    for k in range(1,N+1):
        
        if state[k][1]==0:
            fail_rate[k][0]=0
        else:
            fail_rate[k][0]=(state[k][0]/(state[k][0]+state[k][1]))
    
    result=fail_rate[1:]
    result.sort(key=lambda x:(-x[0],x[1]))
    result=deque(result)
    
    answer=[]
    while result:
        u,v=result.popleft()
        answer.append(v)
    

    return answer
