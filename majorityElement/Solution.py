from collections import Counter
from typing import List

# Solution クラスに majorityElement メソッドを実装
class Solution:
    # 引数 nums は整数のリスト
    # 戻り値は nums 中で過半数を占める要素
    def majorityElement(self, nums: List[int]) -> int:
        # nums の要素の出現回数をカウントするため、Counter クラスを使用
        ans = Counter(nums)
        # most_common(1) は最も頻繁に出現する要素をリストで返す
        # その最初の要素（頻度の高い要素）の値を返す
        return ans.most_common(1)[0][0]

# main 関数の定義
def main():
    # テスト用の配列を用意。例: [3, 2, 3] の場合、3 が過半数を占める要素
    test_case1 = [3, 2, 3]  # 過半数を占める要素は 3
    test_case2 = [2, 2, 1, 1, 1, 2, 2]  # 過半数を占める要素は 2

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # test_case1 で majorityElement メソッドを呼び出し、結果を表示
    result1 = solution.majorityElement(test_case1)
    print(f"Test case 1: {test_case1}, Majority element: {result1}")

    # test_case2 で majorityElement メソッドを呼び出し、結果を表示
    result2 = solution.majorityElement(test_case2)
    print(f"Test case 2: {test_case2}, Majority element: {result2}")

# スクリプトが直接実行された場合に main 関数を実行する
if __name__ == "__main__":
    main()
