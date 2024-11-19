def matrix_sum(N, matrix):
 
    row_sums = [sum(row) for row in matrix]
    

    column_sums = [sum(matrix[i][j] for i in range(N)) for j in range(N)]
   
    A = [row_sums[i] + column_sums[i] for i in range(N)]
    
    print(" ".join(map(str, A)))


N = int(input()) 
matrix = [list(map(int, input().split())) for _ in range(N)]


matrix_sum(N, matrix)
