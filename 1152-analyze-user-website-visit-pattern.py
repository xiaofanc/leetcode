"""
- order of visiting the websites matters!
- combinations(values, 3) will keep the order
- each user can only count once for each pattern!

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            users[user].append(web)
        # print("users", users)
        patterns = {}
        # count users for each pattern
        for key, values in users.items():
            # get all possible 3-sequences combinations(values, 3)
            # count each one once for one user
            visited = set()
            for comb in itertools.combinations(values, 3):
                if comb not in visited:
                    patterns[comb] = patterns.get(comb, 0) + 1
                visited.add(comb)
        
        # return the pattern with the most frequency
        # if same frequency, return lexicographically smallest
        return max(sorted(patterns), key=patterns.get)
            
if __name__ == '__main__':
    s = Solution()
    print(s.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"])) # ["home","about","career"]


    