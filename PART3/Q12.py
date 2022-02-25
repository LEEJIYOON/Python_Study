from collections import deque


#a=0 기둥, a=1 보
#b=0 삭제, b=1 설치

# 기둥은 바닥 위 or 보의 위 or 다른 기둥 위
# 보는 기둥 위 or 양쪽 끝 부분이 다른 보와 동시 연결

result=[]

def possible(answer):
    global result
    check=deque(answer)

    while check:
        x,y,a=check.popleft()

        if a==0:

            if y==0 or [x-1,y,1] in result or [x,y-1,0] in result or [x,y,1] in result:
                continue
            return False

        else:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                continue
            return False
        
    return True





def solution(n, build_frame):
    global result
    
    for x,y,a,b in build_frame:
        
        if b==1:
            result.append([x,y,a])
            if possible(result):
                pass
            else:
                result.remove([x,y,a])
        
        elif b==0:
            result.remove([x,y,a])
            if possible(result):
                pass
            else:
                result.append([x,y,a])
    
    
    result.sort()
    
    
    return result
