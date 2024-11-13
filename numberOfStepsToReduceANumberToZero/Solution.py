class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2 
            else:
                num -=1 
            steps += 1
        return steps

# 呼び出し部分
if __name__ == "__main__":
    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # サンプル入力
    num = 14

    # メソッドを呼び出し、結果を取得
    result = solution.numberOfSteps(num)

    # 結果を出力
    print(f"Number of steps to reduce {num} to zero:", result)
