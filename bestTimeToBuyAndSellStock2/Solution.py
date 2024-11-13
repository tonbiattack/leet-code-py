from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

# テスト関数


def test_max_profit():
    # テストケースを定義
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1]
    ]

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # 各テストケースで maxProfit を呼び出し、結果を表示
    for prices in test_cases:
        print(f"Input prices: {prices}")
        result = solution.maxProfit(prices)
        print(f"Maximum Profit: {result}\n")


# main 関数
if __name__ == "__main__":
    test_max_profit()
