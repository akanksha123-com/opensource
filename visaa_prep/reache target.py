def runs_to_win(X, Y):
    return X - Y + 1


T = int(input())


results = []


for _ in range(T):
   
    X, Y = map(int, input().split())
    
  
    results.append(runs_to_win(X, Y))


for result in results:
    print(result)
