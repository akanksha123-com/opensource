
X, N = map(int, input().split())
total_planes_needed = (N + 99) // 100  
planes_to_buy = max(0, total_planes_needed - X)
print(planes_to_buy)
