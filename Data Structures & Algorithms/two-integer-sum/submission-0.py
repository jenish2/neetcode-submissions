class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i in range(len(nums)):
            if value_index.get(nums[i]) is None:
                value_index[nums[i]]  = i
        

        for i in range(len(nums)):
            diff = target - nums[i]
            other_index = value_index.get(diff) 
            if other_index is not None and i != other_index:
                return [i,other_index] if i < other_index else [other_index,i]