def calculate_score(X, N):
    return (X // 10) * N
T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    print(calculate_score(X, N))


