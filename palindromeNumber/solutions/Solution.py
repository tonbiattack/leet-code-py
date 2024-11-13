class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負の数は回文にはなりえないため、Falseを返す
        if x < 0:
            return False

        # 変数reversed_numに元の数字xを逆にしたものを保存する
        reversed_num = 0
        temp = x  # 元の数値を保持するためにtemp変数を作成

        # 数字を逆転させるためのループ
        while temp != 0:
            # tempの最下位桁を取得（10で割った余り）
            digit = temp % 10
            # reversed_numにその桁を追加して逆の数を構築
            reversed_num = reversed_num * 10 + digit
            # tempの最下位桁を削除（整数除算）
            temp //= 10

        # 逆転させた数と元の数が同じであれば回文である
        return reversed_num == x

# 呼び出し箇所

# Solutionクラスのインスタンスを作成
solution = Solution()

# 121という数が回文かどうかを確認
x = 1121
result = solution.isPalindrome(x)
print(f"Is {x} a palindrome? {result}")  # 出力: True

# -121という負の数は回文ではないためFalse
x = -121
result = solution.isPalindrome(x)
print(f"Is {x} a palindrome? {result}")  # 出力: False
