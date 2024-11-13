class Solution:
    # 詳細解説：
    # 初期化:

    # maxLength: 最長の重複のない部分文字列の長さを格納する変数を0に初期化します。
    # charSet: 現在の部分文字列に含まれている文字を記録するためのセットです。重複チェックに使います。
    # left: スライディングウィンドウの左端を示すポインタで、初期値は0です。
    # スライディングウィンドウの右端の動き:

    # for right in range(n): rightポインタを0から文字列の長さ n まで順に進め、ウィンドウの右端とします。
    # 重複チェック:

    # if s[right] not in charSet: rightが指す文字がセットにない場合、それをセットに追加し、ウィンドウ内の文字が全て異なる状態を保ちます。
    # 長さの更新: maxLength = max(maxLength, right - left + 1)で現在のウィンドウの長さと最大長を比較し、maxLengthを更新します。
    # 重複処理:

    # while s[right] in charSet: rightが指す文字がセットに既に存在する場合、leftポインタを右に動かし、セットから重複している文字を削除して重複の解消を行います。
    # left += 1で左端を動かし、部分文字列から重複している文字を取り除きます。
    # 最終的な返却:

    # 最後に maxLength を返すことで、最長の重複のない部分文字列の長さが得られます。
    # この実装のポイントは「スライディングウィンドウとセットを利用した重複の管理」です。セットで重複チェックを行うため、効率的に部分文字列の長さを計算できます。
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 文字列の長さを取得
        n = len(s)

        # 最大長を記録する変数
        maxLength = 0

        # 現在の部分文字列に含まれている文字を保存するセット
        charSet = set()

        # スライディングウィンドウの左端を示すポインタ
        left = 0

        # スライディングウィンドウの右端を示すポインタをループで動かす
        for right in range(n):
            # 右端の文字がセットにない場合、重複がないので追加
            if s[right] not in charSet:
                # 現在の文字をセットに追加
                charSet.add(s[right])

                # 現在の部分文字列の長さを計算して最大長を更新
                maxLength = max(maxLength, right - left + 1)

            else:
                # 重複がある場合、左端のポインタを動かして重複がなくなるまでセットから削除
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1

                # 重複がなくなったら、右端の文字をセットに追加
                charSet.add(s[right])

        # 最大の部分文字列の長さを返す
        return maxLength


# 呼び出し例
solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)  # 3（重複なしの最長部分文字列 "abc" の長さ）
