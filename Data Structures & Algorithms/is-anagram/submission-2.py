class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        size = len(set(s)) or 1
        my_map = [[] for _ in range(size)]

        # count characters in s
        for char in s:
            bucket = my_map[ord(char) % size]
            for pair in bucket:
                if pair[0] == char:
                    pair[1] += 1
                    break
            else:
                bucket.append([char, 1])

        # subtract characters in t
        for char in t:
            bucket = my_map[ord(char) % size]
            for pair in bucket:
                if pair[0] == char:
                    pair[1] -= 1
                    if pair[1] < 0:      # t has more of this char than s
                        return False
                    break
            else:
                return False             # t has a char that s doesn't

        return True

            

        