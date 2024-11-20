X, Y, Z = map(int, input().split())

total_time_needed = X * Y
total_available_time = Z * 1440


if total_time_needed <= total_available_time:
    print("YES")
else:
    print("NO")
