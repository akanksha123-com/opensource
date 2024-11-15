N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
mirrored_matrix = [row[::-1] for row in matrix]
for row in mirrored_matrix:
    print(" ".join(map(str, row)))
