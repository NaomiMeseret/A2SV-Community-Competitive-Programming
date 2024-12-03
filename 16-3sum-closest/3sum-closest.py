class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum=float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                current_sum=nums[left]+nums[i]+nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum

            