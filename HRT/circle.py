"""
find all non-negative integer points that in the circle
"""
def solution(x, y, r):
    left, right, up, bottom = x-r, x+r, y+r, y-r
    res = 0
    # for i in range(max(left, 0), right+1):
    #     for j in range(max(bottom, 0), up+1):
    #         if (i-x)**2 + (j-y)**2 <= r**2:
    #             res += 1
                
    for i in range(max(left, 0), right+1):
        jmax = r**2 - (i-x)**2
        a = y - int(math.sqrt(jmax))
        b = int(math.sqrt(jmax)) + y 
        if b >= max(a, 0):
            res += b - max(a, 0) + 1
    return res
                
                
