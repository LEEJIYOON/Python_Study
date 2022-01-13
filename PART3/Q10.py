from copy import deepcopy

def solution(key, lock):
    

    

    
    
    
    
    M=len(key)
    N=len(lock)
    
    #초기 검사
    
    init_answer=0
    for i in lock:
        init_answer+=sum(i)
    
    if init_answer==N**2:
        return True
    
    
    
    def rotate_90(m):
        K=len(m)
        ret=[[0]*K for _ in range(K)]
        
        for r in range(K):
            for c in range(K):
                ret[c][K-1-r]=m[r][c]
        return ret
                
    lock_hole=[]
    
    for a in range(N):
        for b in range(N):
            if lock[a][b]==0:
                lock_hole.append((a,b))
                

    
    # 처음 그대로
    
    lock_copy=deepcopy(lock)
    
        
    key_dolgi=[]
    check=0
    
    for a in range(M):
        for b in range(M):
            if key[a][b]==1:
                key_dolgi.append((a,b))
    
    
    for i in lock_hole:
        for k in key_dolgi:
            x_gap=i[0]-k[0]
            y_gap=i[1]-k[1]
            
            for j in key_dolgi:
                if j[0]+x_gap < N and j[0]+x_gap >=0 and j[1]+y_gap <N and j[1]+y_gap>=0:
                    lock_copy[j[0]+x_gap][j[1]+y_gap]+=1
            
            answer=0
            check=0
            for f in lock_copy:
                answer+=sum(f)
                check=max(check,max(f))
            
            if answer==N**2 and check==1:
                return True
            else:
                lock_copy=deepcopy(lock)
    
    
    
    # 1번 회전
    key=rotate_90(key)    
    lock_copy=deepcopy(lock)
    
        
    key_dolgi=[]
    check=0
    
    for a in range(M):
        for b in range(M):
            if key[a][b]==1:
                key_dolgi.append((a,b))
    
    
    for i in lock_hole:
        for k in key_dolgi:
            x_gap=i[0]-k[0]
            y_gap=i[1]-k[1]
            
            for j in key_dolgi:
                if j[0]+x_gap < N and j[0]+x_gap >=0 and j[1]+y_gap <N and j[1]+y_gap>=0:
                    lock_copy[j[0]+x_gap][j[1]+y_gap]+=1
            
            answer=0
            check=0
            for f in lock_copy:
                answer+=sum(f)
                check=max(check,max(f))
            
            if answer==N**2 and check==1:
                return True
            else:
                lock_copy=deepcopy(lock)
    # 2번 회전
    key=rotate_90(key)
    lock_copy=deepcopy(lock)
    
        
    key_dolgi=[]
    check=0
    
    for a in range(M):
        for b in range(M):
            if key[a][b]==1:
                key_dolgi.append((a,b))
    
    
    for i in lock_hole:
        for k in key_dolgi:
            x_gap=i[0]-k[0]
            y_gap=i[1]-k[1]
            
            for j in key_dolgi:
                if j[0]+x_gap < N and j[0]+x_gap >=0 and j[1]+y_gap <N and j[1]+y_gap>=0:
                    lock_copy[j[0]+x_gap][j[1]+y_gap]+=1
            
            answer=0
            check=0
            for f in lock_copy:
                answer+=sum(f)
                check=max(check,max(f))
            
            if answer==N**2 and check==1:
                return True
            else:
                lock_copy=deepcopy(lock)
    
    # 3번 회전
    key=rotate_90(key)
    lock_copy=deepcopy(lock)
    
        
    key_dolgi=[]
    check=0
    
    for a in range(M):
        for b in range(M):
            if key[a][b]==1:
                key_dolgi.append((a,b))
    
    
    for i in lock_hole:
        for k in key_dolgi:
            x_gap=i[0]-k[0]
            y_gap=i[1]-k[1]
            
            for j in key_dolgi:
                if j[0]+x_gap < N and j[0]+x_gap >=0 and j[1]+y_gap <N and j[1]+y_gap>=0:
                    lock_copy[j[0]+x_gap][j[1]+y_gap]+=1
            
            answer=0
            check=0
            for f in lock_copy:
                answer+=sum(f)
                check=max(check,max(f))
            
            if answer==N**2 and check==1:
                return True
            else:
                lock_copy=deepcopy(lock)
    
    # 회전 다해도 답 없음
    
    return False
