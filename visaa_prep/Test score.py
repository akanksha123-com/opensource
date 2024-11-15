def can_achieve_marks(N, X, Y):
    for a in range(N + 1):
        b = N - a
        if a * X + b * 8 == Y:
            return "YES"
    return "NO"


N, X, Y = map(int, input().split())

print(can_achieve_marks(N, X, Y))
