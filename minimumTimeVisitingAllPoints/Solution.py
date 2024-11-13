from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        与えられたポイントリストを順番に訪問するために必要な最小時間を計算します。
        各ステップでは、対角方向、水平方向、または垂直方向に1単位移動できます。
        """
        sec = 0  # 合計時間を保持する変数
        x1, y1 = points.pop()  # 最初のポイントを取得し、そのx, y座標をx1, y1に格納
        while points:  # 残りのポイントがある限り処理を続ける
            x2, y2 = points.pop()  # 次のポイントを取得し、そのx, y座標をx2, y2に格納
            # 現在のポイントから次のポイントまでの最大距離を計算
            sec += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2  # 次の比較のためにx1, y1を更新
        return sec  # 最小時間を返す

# 呼び出し箇所
if __name__ == "__main__":
    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # サンプル入力のポイントリスト
    points = [[1, 1], [3, 4], [-1, 0]]

    # メソッドを呼び出し、結果を取得
    result = solution.minTimeToVisitAllPoints(points)

    # 結果を出力
    print("Minimum time to visit all points:", result)
