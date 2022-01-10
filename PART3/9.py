def solution(s):
    
    n=len(s)
    
    min_length=n
    
    for i in range(1,n+1):
        j=0
        new_length=0
        same_number=1
        
        while j < n:
            same_number=1
            
            while s[j:j+i]==s[j+i:j+i+i]:
                same_number+=1
                j=j+i
                
            if same_number==1:
                new_length+=len(s[j:j+i])
            else:
                new_length+=len(str(same_number))+i
            j=j+i
        
        min_length=min(min_length,new_length)
         
        
    
    
    return min_length
