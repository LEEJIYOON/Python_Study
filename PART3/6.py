#kakao, pass the all accuray but just 1 efficiency

def solution(food_times, k):
    
    length=len(food_times)
    min_value=min(food_times)
    total=sum(food_times)
    
    if k>=total:
        return -1
    
    max_cycle=k//length
    time=0
    
    if max_cycle <= min_value:
        for i in range(length):
            food_times[i]-=max_cycle
        
        time=max_cycle*length
    
    else:
        for i in range(length):
            food_times[i]-=min_value
        time=min_value*length
    
    start=0
    answer=0

    
    while time <=k:
        for i in range(start,length):
            start=i+1
            if food_times[i]>0:
                food_times[i]-=1
                answer=i+1
                start=i+1
                if start==length:
                    start=0
                break
        time+=1
        if start==length:
            start=0
            time-=1
    
    if answer==0:
        return 1

    return answer
