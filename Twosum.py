class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i , n in enumerate(nums):
            dif = target - n
            if dif in hm:
                return [hm[dif], i]
            hm[n]= i
        return