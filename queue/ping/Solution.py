class RecentCounter:
    # 初期化メソッド
    def __init__(self):
        # pingリクエストの記録を保持するためのリスト
        # ここに「ping」が呼び出されるたびにリクエスト時間（ミリ秒）を追加します。
        self.records = []
        # 開始位置を示すインデックス（3000ミリ秒の範囲を管理するためのインデックスです）
        self.start = 0

    # pingメソッド: リクエストを記録し、直近3000ミリ秒のリクエスト数を返します。
    def ping(self, t: int) -> int:
        # リクエストを記録（リストに追加）
        self.records.append(t)
        
        # 3000ミリ秒の範囲外の古いリクエストを削除するために「start」を更新
        # リスト内の値が「t - 3000」より小さい場合、それは3000ミリ秒より前のリクエストなので
        # これを含まないように「start」インデックスをインクリメントして古いリクエストをスキップします。
        while self.records[self.start] < t - 3000:
            self.start += 1

        # 「start」から「records」の最後までの長さが直近3000ミリ秒のリクエスト数です。
        return len(self.records) - self.start

# インスタンスを作成し、pingメソッドを呼び出して確認します。
recent_counter = RecentCounter()
print(recent_counter.ping(1))    # 初めてのリクエスト、結果は1
print(recent_counter.ping(100))  # 2つ目のリクエスト、まだ3000ミリ秒の範囲内なので結果は2
print(recent_counter.ping(3001)) # 3つ目のリクエスト、最初のリクエスト（t=1）は範囲外になるので結果は3
print(recent_counter.ping(3002)) # 4つ目のリクエスト、最初のリクエストは範囲外のままなので結果は3
