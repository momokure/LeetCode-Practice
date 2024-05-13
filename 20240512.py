# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Easy

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s: #文字列sの文字charを回す
            
            if stack and stack[-1] == char:
                # 文字列内の各文字に対して、stackの最後の文字と現在の文字が同じ場合は、stackから文字を取り除く。
                stack.pop()
            else:
                # そうでない場合は、現在の文字をスタックに追加します。
                stack.append(char)
        return ''.join(stack)
    
# 時間計算量 (TC):
# 文字列内の各文字に対してスタック操作を行うため、文字列の長さを N とすると、
# TC は O(N) です。これは線形時間の計算量です。

# 空間計算量 (SC):
# このアルゴリズムでは、スタックを使用して文字列内の文字を追跡します。
# 最悪の場合、スタックには文字列全体が格納される可能性があります。
# したがって、SC は文字列の長さに比例し、O(N) です。