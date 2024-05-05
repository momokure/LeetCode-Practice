# https://leetcode.com/problems/swap-salary/description/
# 627. Swap Salary


UPDATE Salary #Salaryテーブルを更新する
SET sex = CASE #CASE文でsexをケース判定処理する
    WHEN sex = 'm' THEN 'f' #sexがmのとき、fに更新する
    WHEN sex = 'f' THEN 'm' #sexがfのとき、mに更新する
    ELSE sex #その他はそのまま
END;
