class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = set()
        for e in nums:
            if e in map1:        # seen this number before → duplicate
                return True
            else:
                map1.add(e)      # first time seeing it → remember it
        return False 
        