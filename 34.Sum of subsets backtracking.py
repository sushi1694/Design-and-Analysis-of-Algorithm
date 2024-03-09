def subset_sum_backtracking(nums, target):
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if current_sum + nums[i] <= target:
                path.append(nums[i])
                backtrack(i + 1, path, current_sum + nums[i])
                path.pop()

    result = []
    nums.sort()
    backtrack(0, [], 0)
    return result

# Example usage
nums = [1, 2, 3, 4]
target_sum = 5

subsets_with_sum = subset_sum_backtracking(nums, target_sum)
print("Subsets with the sum of", target_sum, "are:")
for subset in subsets_with_sum:
    print(subset)
