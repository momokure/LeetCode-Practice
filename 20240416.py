# 392. Is Subsequence
# Easy
# https://leetcode.com/problems/is-subsequence/?source=submission-noac
# 自力

# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        i, j = 0, 0
        for i in range(len(list_t)-1):
            #print(list_t[i],",",list_s[j])
            if list_t[i] == list_s[j]:           
                if j < len(list_s)-1:
                    j+=1
                else:
                    return True
            elif i >= len(list_t)-1:
                return False

        # #模範解答
        # s_pointer = 0
        # t_pointer = 0
    
        # # 両方の文字列で繰り返し
        # while s_pointer < len(s) and t_pointer < len(t):
        #     # 文字がマッチしたら、次の文字に移動する
        #     if s[s_pointer] == t[t_pointer]:
        #         s_pointer += 1
        #     # tはいずれにしても次の文字に移動する
        #     t_pointer += 1
        
        # # もしsのすべての文字がtに見つかったら、sはtの部分集合。
        # return s_pointer == len(s)

        #学び。
        #- 文字列を処理する際には配列(リスト)化する。
        #- リストのインデックスをポインターという概念で捉え、ポインターの移動距離とリストsの長さが同じになったことを持って部分集合である判定を行う。