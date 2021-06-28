class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])
        
if __name__ == '__main__':
    s = Solution()
    print(s.maximumWealth([[1,2,3],[3,2,1]]))
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))