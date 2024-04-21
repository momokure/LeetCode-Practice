# 999. Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/description/


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r_x = 0
        r_y = 0
        num = 0
        for y, row in enumerate(board):  
            try:
                r_x = row.index("R")
                r_y = y
                
                break
            except ValueError:
                pass
        print(r_y,r_x)
        x = r_x + 1
        while x < 8:
            print(r_y,x)
            print(board[r_y][x])
            if board[r_y][x] == "p":
                num += 1
                break
            elif board[r_y][x] == "B":
                break
            x += 1
        x = r_x - 1
        while x >= 0:
            print(r_y,x)
            print(board[r_y][x])
            if board[r_y][x] == "p":
                num += 1
                break
            elif board[r_y][x] == "B":
                break
            x -= 1
        y = r_y +1
        while y < 8:
            print(y,r_x)
            print(board[y][r_x])
            if board[y][r_x] == "p":
                num += 1
                break
            elif board[y][r_x] == "B":
                break
            y += 1
        y = r_y -1
        while y >= 0:
            print(y,r_x)
            print(board[y][r_x])
            if board[y][r_x] == "p":
                num += 1
                break
            elif board[y][r_x] == "B":
                break
            y -= 1
        return num
#
# [ Time taken: 1 hr 3 m 49 s ]
# このコードは、与えられた8x8のチェスボード上でルークがどれだけポーンを
# 捕まえることができるかを数える関数を実装していますね。この関数の
# 時間計算量 (Time Complexity, TC) と空間計算量 (Space Complexity, SC) 
# について説明します。まず、時間計算量 (TC) です。この関数は、チェスボードの
# 各マスを一度だけチェックします。したがって、ボードのサイズが固定されている場合、
# ルークがポーンを捕まえることができる可能性があるマスをチェックする必要がありますが、
# その数は固定されています。したがって、この関数の時間計算量は O(1) です。
# 次に、空間計算量 (SC) です。この関数は、追加のデータ構造を作成せず、
# 与えられた入力のみを使用します。したがって、追加のメモリ使用量はなく、
# 関数の空間計算量は O(1) です。

# したがって、この関数の時間計算量は O(1) であり、空間計算量も O(1) です。