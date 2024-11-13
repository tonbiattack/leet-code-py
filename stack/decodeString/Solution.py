class Solution(object):
    def decodeString(self, s):
        # スタックを初期化して、現在の数字（curNum）と現在の文字列（curString）を設定
        stack = []
        curNum = 0
        curString = ''
        
        # 文字列の各文字を1文字ずつ処理していく
        for c in s:
            # 現在の文字が'['の場合：
            # 1. 現在の文字列（curString）をスタックに保存（ネストされた文字列が始まるため）
            # 2. 現在の数値（curNum）をスタックに保存
            # 3. 現在の文字列と数値をリセットする
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            
            # 現在の文字が']'の場合：
            # 1. スタックから数値を取り出し、これを`num`に設定
            # 2. スタックから前の文字列を取り出し、これを`prevString`に設定
            # 3. 現在の文字列を`prevString + num * curString`に設定して、デコードされた文字列を作成
            elif c == ']':
                num = stack.pop()         # 繰り返し回数を取得
                prevString = stack.pop()   # 前の文字列を取得
                curString = prevString + num * curString  # デコードした文字列を生成
            
            # 現在の文字が数字の場合：
            # 1. 数値の桁が複数ある場合に対応するため、`curNum`を更新
            # 2. 例えば「10[a]」の場合、'1'の後に'0'がきたとき10として認識する
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            
            # 現在の文字が通常の文字（アルファベットなど）の場合：
            # 1. 現在の文字列に文字を追加する
            else:
                curString += c
        
        # 完成した現在の文字列を返す
        return curString

# 使用例
solution = Solution()
decoded_string = solution.decodeString("3[a]2[bc]")
print(decoded_string)  # 期待する出力: "aaabcbc"
