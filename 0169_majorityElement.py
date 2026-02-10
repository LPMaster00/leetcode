class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        frequency = 0
        for i in range(len(nums)):
            if answer == nums[i]:
                frequency += 1
            else:
                if frequency == 0:
                    answer = nums[i]
                else:
                    frequency -= 1
        return answer
