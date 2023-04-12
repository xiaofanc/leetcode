"""
You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two different indices i < j, such that a[i] + a[j] is divisible by k.
For a = [1, 2, 3, 4, 5] and k = 3, the output should be solution(a, k) = 4.
There are 4 pairs of numbers that sum to a multiple of k = 3:

a[0] + a[1] = 1 + 2 = 3
a[0] + a[4] = 1 + 5 = 6
a[1] + a[3] = 2 + 4 = 6
a[3] + a[4] = 4 + 5 = 9

Guaranteed constraints:
1 ≤ a.length ≤ 10**5,
1 ≤ a[i] ≤ 10**9

Guaranteed constraints:
1 ≤ k ≤ 10**9

"""
# TLE: 6/11 passed
def solution(a, k):
    res = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) % k == 0:
                res += 1
    return res

# MLE: 9/11
def solution(a, k):
    count = 0
    reminder = [0] * k
    
    for num in a:
        reminder[num % k] += 1
    
    # for all possible reminders
    for i in range(1, k//2+1):
        if i != k - i:
            count += reminder[i] * reminder[k-i]
        else:
            # select pairs of elements from a set of n elements without replacement
            count += reminder[i] * (reminder[i]-1) // 2
    
    count += reminder[0] * (reminder[0]-1) // 2
    
    return count

# TLE: 9/11
def solution(a, k):
    count = 0
    cnt = {}
    
    for num in a:
        remainder = num % k
        if remainder in cnt:
            cnt[remainder] += 1
        else:
            cnt[remainder] = 1
    
    for i in range(1, k//2+1):
        if i != k - i:
            if i in cnt and k-i in cnt:
                count += cnt[i] * cnt[k-i]
        else:
            if i in cnt:
                count += cnt[i] * (cnt[i]-1) // 2
    
    if 0 in cnt:
        count += cnt[0] * (cnt[0]-1) // 2
    
    return count





