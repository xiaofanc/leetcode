"""
For any particular difficulty level, what can be the optimal strategy to complete the tasks using minimum rounds?
When can we not complete all tasks of a difficulty level?
"""

class Solution:
	# 56 / 79 testcases passed
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)

        def findRound(task):
            # 3*i + 2*j = task, find the min(i+j)
            def dfs(i, j, task):
                res = 3*i + 2*j
                if res == task:
                    return i+j
                if res > task:
                    return -1
                cnt = 0
                for m in range(i+1, task//3+1):
                    cnt = dfs(m, j, task)
                    if cnt > 0 or cnt == -1:
                        return cnt
                return cnt
        
            for j in range(0, task//2+1):
                cnt = dfs(0, j, task)
                if cnt > 0:
                    return cnt
            return -1

        res = 0
        for k, v in count.items():
            if findRound(v) == -1:
                return -1
            else:
                res += findRound(v)
        return res


    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)

        def findRound(task):
            # 3*i + 2*j = task, find the min(i+j)
            for j in range(task//2+1):
                for i in range(task//3+1):
                    if 3*i + 2*j == task:
                        return i+j
                    elif 3*i + 2*j > task:
                        break
            return -1
            
        res = 0
        for k, v in count.items():
            if findRound(v) == -1:
                return -1
            else:
                res += findRound(v)
        return res

    def minimumRounds(self, tasks: List[int]) -> int:
        # we can divide the counts into three groups:
        # Integers that are multiples of 3 i.e., of the form 3*K. We need min K rounds
        # Integers that leaves remainder of 1 when divided by 3 i.e., of the form 3*K+1. We need min K+1 rounds. 3*K+1 = 3*(K-1)+2*2
        # Integers that leaves remainder of 2 when divided by 3 i.e., of the form 3*K+2. We need min K+1 rounds.
        count = collections.Counter(tasks)
        res = 0
        for k, v in count.items():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += v//3
            elif v % 3 == 1 or v % 3 == 2:
                res += v//3 + 1
        return res

        
                        