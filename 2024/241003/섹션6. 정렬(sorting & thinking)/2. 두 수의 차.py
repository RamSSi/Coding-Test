def solution(nums):
    answer = []
    nums.sort()
    gap = 10000000
    for i in range (len(nums)-1):
        if nums[i+1] - nums[i] < gap:
            gap = nums[i+1] - nums[i]
            answer = [[nums[i],nums[i+1]]]
        elif nums[i+1] - nums[i] == gap:
            answer.append([nums[i], nums[i+1]])           
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
