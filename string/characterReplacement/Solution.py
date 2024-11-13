class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 変数の初期化
        # l: 左側のポインタを示す変数、スライディングウィンドウの左端
        l = 0
        # c_frequency: 各文字の出現回数をカウントするための辞書
        c_frequency = {}
        # longest_str_len: 最長の文字置換によって作れる連続部分文字列の長さ
        longest_str_len = 0

        # スライディングウィンドウを右側に拡張していくループ
        for r in range(len(s)):
            # 新たにs[r]がc_frequencyにない場合、0に初期化
            if s[r] not in c_frequency:
                c_frequency[s[r]] = 0
            # 現在の文字 s[r] の出現回数をインクリメント
            c_frequency[s[r]] += 1

            # スライディングウィンドウの幅
            cells_count = r - l + 1
            # 現在のスライディングウィンドウ内で、最も出現回数が多い文字の頻度を取得
            max_frequency = max(c_frequency.values())

            # 最大頻度文字以外を置換するコストが k 以下である場合、現在のウィンドウは条件を満たしている
            if cells_count - max_frequency <= k:
                # 条件を満たすウィンドウの長さが最大ならば、longest_str_lenを更新
                longest_str_len = max(longest_str_len, cells_count)
            else:
                # 置換コストがkを超える場合は、左端の文字を削除し、左端ポインタ(l)を1つ右に移動
                c_frequency[s[l]] -= 1
                # もしその文字のカウントが0になったら、辞書から削除して管理
                if c_frequency[s[l]] == 0:
                    c_frequency.pop(s[l])
                l += 1  # ウィンドウを狭めるために左端を右に移動

        # 条件を満たす最長の連続部分文字列の長さを返す
        return longest_str_len


    # 呼び出し箇所
if __name__ == "__main__":
    # Solution クラスのインスタンスを作成
    solution = Solution()

    # テストケース
    s = "AABABBA"
    k = 1

    # characterReplacement 関数を呼び出し、結果を出力
    result = solution.characterReplacement(s, k)
    print(f"Input: s = '{s}', k = {k}")
    print(f"Output: {result}")  # 期待される出力は 4
