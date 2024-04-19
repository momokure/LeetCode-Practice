# 2455. Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
# Easy

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        #positive integer divisible by 6
        list_div6 = []
        output = 0
        for i in nums:
            if i % 6 == 0 and i > 0:
                list_div6.append(i)
        if len(list_div6) != 0:
            output = math.floor(sum(list_div6)/len(list_div6))
            return output
        else:
            return 0

#12:22で解けた！