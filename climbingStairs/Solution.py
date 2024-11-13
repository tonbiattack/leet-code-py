class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1+num2
        return num2
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(3))