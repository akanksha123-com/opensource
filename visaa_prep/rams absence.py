def max_absent_streak(n, attendance):
    max_streak = 0
    current_streak = 0
    
    for day in attendance:
        if day == 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)  
        else:
            current_streak = 0 
    
    return max_streak


N = int(input())
attendance = list(map(int, input().split()))  

print(max_absent_streak(N, attendance))
