class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for t, c, n in items:
            if ruleKey == "type":
                if t == ruleValue:
                    res += 1
            elif ruleKey == "color":
                if c == ruleValue:
                    res += 1
            else:
                if n == ruleValue:
                    res += 1
        return res

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {"type": 0, "color": 1, "name": 2}
        idx = rule[ruleKey]
        return len([item for item in items if item[idx] == ruleValue])

                       
if __name__ == '__main__':
    s = Solution()
    print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))