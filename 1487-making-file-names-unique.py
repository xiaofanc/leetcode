class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        exists = set()
        last = defaultdict(int)
        for name in names:
            k = last[name]
            modified = name
            while modified in exists:
                k += 1
                modified = f"{name}({k})"
            ans.append(modified)
            exists.add(modified)
            last[name] = k
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.getFolderNames(["gta","gta(1)","gta","avalon"]))
    print(s.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))