n = int(input().strip())
arr = list(map(int, input().strip().split()))
balance_array = []
for i in range(n):
    left_weight = sum(arr[:i]) 
    right_weight = sum(arr[i+1:])  
    balance_array.append(abs(left_weight - right_weight))
print(" ".join(map(str, balance_array)))
