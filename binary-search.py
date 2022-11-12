from bisect import bisect_left, bisect_right, bisect

def bs(l, target):
    left, right = 0, len(l)-1
    while left <= right:
        mid = left + (right - left) // 2
        #print(left, right, mid)
        if target < l[mid]:
            right = mid-1
        elif target > l[mid]:
            left = mid+1
        else:
            return mid
    return -1

# 寻找左侧边界
def left_bound(l target):
    left, right = 0, len(l)-1
    while left <= right:
        mid = left + (right - left) // 2
        #print(left, right, mid)
        if target < l[mid]:
            right = mid-1
        elif target > l[mid]:
            left = mid+1
        elif target == l[mid]:
            right = mid-1
    if l[left] != target or left >= len(l):
        return -1
    return left

# 寻找右侧边界 [1,2,2,2,3]
def right_bound(l target):
    left, right = 0, len(l)-1
    while left <= right:
        mid = left + (right - left) // 2
        #print(left, right, mid)
        if target < l[mid]:
            right = mid-1
        elif target > l[mid]:
            left = mid+1
        elif target == l[mid]:
            left = mid+1
    if l[right] != target or right < 0:
        return -1
    return right

# 找到第一个 >= target的数
def bs_left(l, target):
    lo, hi = 0, len(l)
    #print(l, target)
    while lo < hi:
        #print(lo, hi, mid)
        mid = (lo+hi)//2
        if l[mid] < target:
            lo = mid+1
        else:
            hi = mid
    return lo

# 找到第一个 > target的数
def bs_right(l, target):
    lo, hi = 0, len(l)
    #print(l, target)
    while lo < hi:
        #print(lo, hi, mid)
        mid = (lo+hi)//2
        if l[mid] > target:
            hi = mid
        else:
            lo = mid+1
    return lo

if __name__ == '__main__':
    #print(bs([1,2,3], 1)) #0 
    #print(bs([1,2,3,4], 3)) #2
    #print(bs([1,2,3,4], 2)) #1
    #print(bs([1,2,3,5,6], 4)) #2
    #print(bs([1,2,3,5,6,7], 4)) #2
    #print(bs([3], 1)) #0

    #[1, 1, 1, 1, 2, 2, 2, 3, 5, 10]
    # 1  2  3  4  5  6  7  8  9
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 1) == 0)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 2) == 4)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 3) == 7)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 4) == 8)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 5) == 8)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 6) == 9)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 7) == 9)
    print(bs_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10],10) == 9)

    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 1) == 4)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 2) == 7)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 3) == 8)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 4) == 8)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 5) == 9)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 6) == 9)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 7) == 9)
    print(bs_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10],10) ==10) # out of bound

    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 1) == 0)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 2) == 4)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 3) == 7)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 4) == 8)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 5) == 8)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 6) == 9)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 7) == 9)
    print(bisect_left([1, 1, 1, 1, 2, 2, 2, 3, 5, 10],10) == 9)

    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 1) == 4)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 2) == 7)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 3) == 8)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 4) == 8)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 5) == 9)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 6) == 9)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 7) == 9)
    print(bisect_right([1, 1, 1, 1, 2, 2, 2, 3, 5, 10],10) ==10)

    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 1) == 4)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 2) == 7)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 3) == 8)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 4) == 8)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 5) == 9)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 6) == 9)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10], 7) == 9)
    print(bisect([1, 1, 1, 1, 2, 2, 2, 3, 5, 10],10) ==10)

