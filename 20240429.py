# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/
# Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        # 辞書を用意する
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        latin = 0
        pointer = 0 # 比較用の変数

        for i in s[::-1]: # リストをリバースでまわす
            if pointer <= dict[i] or pointer == 0: # もしpointerが辞書のi文字目以下 or 0なら
                latin += dict[i] # latinに辞書のi文字目を足して代入
                pointer = dict[i] # pointerに辞書のi文字目を代入する
            else: # もしpointerが辞書のi文字目より大きかったら
                latin -= dict[i] # latinにlatinから辞書のi文字目を引いた数を代入
        return latin
    

    # TC: 0(1)
    # SC: 0(n)