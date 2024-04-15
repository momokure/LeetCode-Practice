# 345. Reverse Vowels of a String
# Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#ChatGPTによる模範解答

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s) #リスト化する
        i, j = 0, len(s) - 1 #iは整数0、jはリストsの長さ（文字列の長さ）マイナス1
        
        while i < j: #iが0から文字列の長さマイナス1まで増える間
            if s[i] in vowels and s[j] in vowels: #母音のいずれかにi文字目が当てはまる、且つ、母音のいずれかにj文字目が当てはまるなら
                s[i], s[j] = s[j], s[i] #i文字目にはj文字目を代入する、j文字目にはi文字目を代入する
                i += 1 #iを1増やす
                j -= 1 #jを1増やす
            elif s[i] in vowels: ##その他のとき、母音のいずれかにi文字目だけが当てはまるなら、
                j -= 1 #jを1減らす
            elif s[j] in vowels: ##その他のとき、母音のいずれかにj文字目だけが当てはまるなら、
                i += 1 #iを1増やす
            else: #その他のとき（母音がi文字目にもj文字目にも当てはまらないとき）
                i += 1 #iを1増やす
                j -= 1 #jを1減らす
        
        return ''.join(s) #リストのsを結合し文字列化する


##ポイント①文字列に配列的な処理をするには、pythonの場合は文字列をリスト化してから処理する
##ポイント②文字列を裏返して処理するときには、１つのループの中で増える変数と減る変数を用意して、頭からとお尻から両側から処理し、ループ処理を最小限に抑える

# この関数の時間計算量（Time Complexity）は、文字列の長さを n とすると 
# O(n) です。これは、文字列を一度だけ反転させるための単純な反復処理です。
# 空間計算量（Space Complexity）は、追加のリストを作成せずに、入力文字列を直接変更するので、 
# O(1) です。追加のデータ構造を作成しないため、メモリの追加使用量は入力文字列のサイズによらず一定です。