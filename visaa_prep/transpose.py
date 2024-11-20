
N = int(input())


matrix = []


for i in range(N):
    row = list(map(int, input().split()))  
    matrix.append(row)


for i in range(N):

    print(" ".join(str(matrix[j][i]) for j in range(N)))
