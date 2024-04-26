# 1413. Minimum Value to Get Positive Step by Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/?source=submission-ac
# Easy

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1  # 最初の正の値
        current_sum = 0 # 合計値
    
        for i in nums:
            #合計値に 配列の値を足す
            current_sum += i 
            # startValue と 1から合計を引いた数のうち大きい方をstartValueに返す
            if startValue < 1 - current_sum: # ex.startValueが0でiの値が-3のとき、0 < 1+3だから startValueに 4を返す
                startValue = 1 - current_sum 
            else: # ex. startValueが4でiの値が-3のとき、4 
                startValue = startValue
        
        return startValue
    
# TC はこのアルゴリズムの時間複雑度は、リストの要素数に比例するため、
# 0(n) です。ただし、追加のメモリスペースはほとんど使用されないので、空間複雑度は O(1) です。