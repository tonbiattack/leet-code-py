from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0  # gasは現在の位置からジャンプできる距離を保持
        for n in nums:
            if gas < 0:
                # gasが負の値になった場合、その位置から先に進めないため、Falseを返す
                return False
            elif n > gas:
                # 現在の位置のジャンプ可能距離nがgasより大きい場合、gasを更新
                gas = n
            # 1ステップ進むので、gasを減らす
            gas -= 1
            
        # 最後まで到達できる場合はTrueを返す
        return True

if __name__ == "__main__":
    solution = Solution()

    # テストケース1: [2,3,1,1,4]
    nums1 = [2, 3, 1, 1, 4]
    print(f"Can jump in nums1? {solution.canJump(nums1)}")  # Expected: True

    # テストケース2: [3,2,1,0,4]
    nums2 = [3, 2, 1, 0, 4]
    print(f"Can jump in nums2? {solution.canJump(nums2)}")  # Expected: False

    # テストケース3: [1,2,3]
    nums3 = [1, 2, 3]
    print(f"Can jump in nums3? {solution.canJump(nums3)}")  # Expected: True

