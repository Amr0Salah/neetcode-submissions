class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = dict()
        for e in nums:
            if e in map1:        # seen this number before → duplicate
                return True
            else:
                map1[e] =1  # first time seeing it → remember it
        return False 
        