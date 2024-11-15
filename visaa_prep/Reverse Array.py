n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(" ".join(map(str, arr[::-1])))
