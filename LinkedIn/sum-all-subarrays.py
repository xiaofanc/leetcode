"""
get the sum of all subarrays
[4,5,6]
sum = 4 + 4+5 + 4+5+6 + 5 + 5+6 + 6
"""

def SubArraySum(arr, n):
    temp,result = 0,0
 
    # Pick starting point
    for i in range(0, n):
 
        # Pick ending point
        temp=0
        for j in range(i, n):
 
            # sum subarray between
            # current starting and
            # ending points
            temp+=arr[j]
            result += temp
    return result

#(n-i) subarrays beginning with arr[i]
#(n-i)*i subarrays where this element is not first element
def SubArraySum(arr, n):
    result = 0
 
    # computing sum of subarray
    # using formula
    for i in range(0, n):
        result += (arr[i] * (i+1) * (n-i))
 
    # return all subarray sum
    return result




    