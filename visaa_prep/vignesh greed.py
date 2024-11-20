def maximum_perimeter_triangle(N, sticks):

    sticks.sort()
    
  
    for i in range(N - 1, 1, -1):
        
        if sticks[i - 2] + sticks[i - 1] > sticks[i]:

            return sticks[i - 2] + sticks[i - 1] + sticks[i]
    

    return -1

N = int(input())  
sticks = list(map(int, input().split()))


print(maximum_perimeter_triangle(N, sticks))
