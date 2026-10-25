class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums) or 1
        my_map = [[] for _ in range(size)]
        for e in nums:
            bucket = my_map[hash(e) % size]
            if e in bucket:
                return True
            bucket.append(e)
        return False