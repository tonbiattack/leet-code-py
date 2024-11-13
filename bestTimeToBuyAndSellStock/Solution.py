from typing import List

# Solution クラスに maxProfit メソッドを実装
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mx: これまでの最大利益, mn: これまでの最低価格
        mx, mn = 0, prices and prices[0]
        
        # 1日目から順に株価を確認
        for i in range(1, len(prices)):
            # 現在の株価が前日の株価よりも高い場合、利益を計算
            if prices[i] > prices[i-1]:
                # 最大利益を更新
                mx = max(mx, prices[i] - mn)
            else:
                # 最低価格を更新
                mn = min(mn, prices[i])
        
        # 最大利益を返す
        return mx

# テスト関数
def test_max_profit():
    # テストケースを定義
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # 1日目に買って5日目に売ると利益5
        [7, 6, 4, 3, 1],     # 株価が下がり続ける場合、利益は0
        [2, 4, 1],           # 2日目に買って4日目に売ると利益2
        [3, 3, 5, 0, 0, 3, 1, 4],  # 5日目に買って8日目に売ると利益4
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
