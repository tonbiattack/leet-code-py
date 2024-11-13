from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 初期化：タンクの総ガソリン量を表す tank、開始位置を表す start、
        # 現在の累積ガソリン量を表す cur を 0 に設定します。
        tank, start, cur = 0, 0, 0

        # ガソリンスタンドを順番に巡回します。
        for i in range(len(gas)):
            # 現在のスタンドでのガソリン供給量とコストの差を計算し、
            # 累積値に加算します。
            gain = gas[i] - cost[i]
            cur += gain
            tank += gain

            # デバッグ用出力（必要に応じてコメントアウト）
            # print(f"ステーション {i}: gain={gain}, cur={cur}, tank={tank}")

            # 累積ガソリン量が負になった場合、現在のスタート位置からは
            # 一周できないため、次のスタンドを新たなスタート位置とします。
            if cur < 0:
                # 現在の累積ガソリン量をリセット
                cur = 0
                # スタート位置を次のインデックスに更新
                start = i + 1
                # デバッグ用出力
                # print(f"累積ガソリンが負になりました。新しいスタート位置は {start} です。")

        # 総ガソリン量が総コストより小さい場合、一周は不可能です。
        if tank < 0:
            # デバッグ用出力
            # print("総ガソリン量が総コストより少ないため、一周は不可能です。")
            return -1
        else:
            # 一周可能なスタート位置を返します。
            return start

def main():
    # 問題の説明：
    # ガソリンスタンドが環状に並んでおり、それぞれのスタンドには供給できるガソリンの量 (gas[i]) と、
    # 次のスタンドまで移動するのに必要なガソリンのコスト (cost[i]) があります。
    # 最初にガソリンタンクが空の状態で、どのスタンドから出発すれば一周できるかを求めます。
    # もし一周できるスタート位置が存在しない場合は -1 を返します。

    # 解説：
    # 1. 全体の総ガソリン量 (sum(gas)) と総コスト (sum(cost)) を比較します。
    #    総ガソリン量が総コストより少ない場合、一周は不可能です。
    # 2. ガソリンスタンドを順番に巡回し、各地点でのガソリンの増減を累積します。
    # 3. 累積ガソリン量が負になった地点では、現在のスタート位置からは一周できないため、
    #    スタート位置を次のスタンドに更新します。
    # 4. 最終的に、一周可能なスタート位置を返します。

    # テストケースの入力
    gas = [1, 2, 3, 4, 5]  # 各スタンドで供給できるガソリンの量
    cost = [3, 4, 5, 1, 2]  # 次のスタンドまで移動するのに必要なガソリンの量

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # メソッドを呼び出して結果を取得
    start_station = solution.canCompleteCircuit(gas, cost)

    # 結果を出力
    if start_station != -1:
        print(f"出発可能な開始位置は: スタンド {start_station} です。")
    else:
        print("一周することは不可能です。")

if __name__ == "__main__":
    main()