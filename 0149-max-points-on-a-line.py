class Solution(object):
    def maxPoints(self, points):
        if len(points) < 2:
            return len(points)
        maxcount = 0
        for i in range(len(points)):
            # every possible slope for points[i]
            cnt = defaultdict(int)
            # starting from i+1 to avoid repeating counting
            for j in range(i+1, len(points)):
                if points[j][0] == points[i][0]:
                    # 1 is points[i]
                    cnt["inf"] = cnt.get("inf", 1) + 1
                    maxcount = max(maxcount, cnt["inf"])
                else:
                    delta = (points[j][1]-points[i][1]) / (points[j][0] - points[i][0])
                    cnt[delta] = cnt.get(delta, 1) + 1
                    maxcount = max(maxcount, cnt[delta])
        return maxcount

