def find_max_average(nums, k):
  
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
   
    for i in range(k, len(nums)):

        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    

    max_average = max_sum / k
    return round(max_average, 4)


n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(f"{find_max_average(nums, k):.4f}")
