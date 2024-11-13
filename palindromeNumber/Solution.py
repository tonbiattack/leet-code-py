class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        整数が回文であるかどうかを判定します。

        回文数は、前から読んでも後ろから読んでも同じ数値になる数です。
        この関数では、まず負の数は回文でないと判断します。
        次に、整数を文字列に変換し、その文字列の両端から中央に向かって
        文字を比較していきます。一つでも一致しない文字があれば、
        その数は回文ではないと判断されます。

        :param x: 判定する整数
        :return: 整数が回文であれば True、そうでなければ False を返します。
        """
        if x < 0:
            return False

        str_x = str(x)
        left, right = 0, len(str_x) - 1

        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1

        return True


# 例としての呼び出し
solution = Solution()
x = 121
result = solution.isPalindrome(x)
print(f"Is {x} a palindrome? {result}")

x = -121
result = solution.isPalindrome(x)
print(f"Is {x} a palindrome? {result}")
