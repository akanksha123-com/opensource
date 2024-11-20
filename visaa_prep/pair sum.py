
def pair_sum(arr, k):
    seen = set() 
    for num in arr:
        if k - num in seen:
            print("true")
            return
        seen.add(num)
    print("false")


N = int(input())  
arr = list(map(int, input().split()))
k = int(input()) 

pair_sum(arr, k)
