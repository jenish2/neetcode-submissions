class Solution:
    def mul_excluded(nums,index_to_skip):
        mul = 1
        for i in range(len(nums)):
            if i != index_to_skip:
                mul *=  nums[i]
        return  mul

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result  = []
        for i in range(len(nums)):
            result.append(Solution.mul_excluded(nums,i))
        return result