# all the other n - 1 people know the celebrity
# the celebrity does not know any of them

class Solution:
    # O(n^2)
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            celebrity = True
            for j in range(n):
                if i != j:
                    # if i knows anyone
                    if knows(i, j):
                        celebrity = False
                        break
                    # if someone does not know i
                    if not knows(j, i):
                        celebrity = False
                        break
            if celebrity:
                return i
        return -1

    # O(n)
    def findCelebrity(self, n: int) -> int:
        def isCelebrity(i):                
            for j in range(n):
                if i != j:
                    if not knows(j, i) or knows(i, j):
                        return False
            return True

        # 1 - find the possible candidate
        # every call of knows(a, b) will rule out a person since if knows(a, b) returns False, b cannot be a celebrity, otherwise, a cannot be a celebrity
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # 2- check if the candidate is celebrity
        if isCelebrity(candidate):
            return candidate
        return -1




