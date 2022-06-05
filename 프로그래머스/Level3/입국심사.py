def solution(n, times):
    answer =0
    max_time = times[-1]*n
    min_time = 1
    now_time = 0
    while min_time < max_time:
        now_time = (min_time+max_time) // 2 
        people = 0
        for time in times:
            people += now_time // time
            
        if people >= n:
            max_time = now_time
        else:
            min_time = now_time + 1
    answer = min_time
    return answer
