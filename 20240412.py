# 345. Reverse Vowels of a String
# Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#自力

# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowels_in_s = []
        s_list = list(s)
        index = 0
        vowels_index_list = []
        #入力された文字列をループ処理
        for i in s:
            #母音があったら
            if (i in vowels):
                #リストに母音のみを順に追加する
                vowels_in_s.append(i)
                vowels_index_list.append(index)
            index +=1 
        #抽出した文字列を逆順にする
        vowels_in_s.reverse()
        replaced_text =[]
        j=0
        for i in range(len(s)):
            if (i in vowels_index_list):
                s_list[i] = vowels_in_s[j]
                print(vowels_in_s)
                j=j+1
        output = ''.join(s_list)
        return str(output)


## 上記はTest case 1 と Test case 2 は通過し、BigO NotationもO(n)だったが、Test case3が通らなかった。
