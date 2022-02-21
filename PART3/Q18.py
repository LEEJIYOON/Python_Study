#function for checking whether string is right or not
def perfect(r): 
    length=len(r)
    count=0
    
    for i in range(length):
        if count <0:
            break
        if r[i]=="(":
            count+=1
        else:
            count-=1
    
    if count==0:
        return True
    
    return False

#function for translation
def reverse_act(s):
    length=len(s)
    answer=""
    
    for i in range(1,length-1):
        if s[i]=="(":
            answer+=")"
        else:
            answer+="("
    
    return answer


def solution(p):
    length=len(p)
    
    if p=="":
        return ""
    
    else:
        count=0
        for i in range(length):
            if p[i]=="(":
                count+=1
            elif p[i]==")":
                count-=1

            if count==0:
                u=p[:i+1]
                v=p[i+1:]
                break

        if perfect(u):
            return u+solution(v)
        else:
            return "("+solution(v)+")"+reverse_act(u)
