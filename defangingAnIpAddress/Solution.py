class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.','[.]')
        return address

if __name__ == "__main__":
    solution = Solution()
    input = "1.1.1.1"
    print(solution.defangIPaddr(input))