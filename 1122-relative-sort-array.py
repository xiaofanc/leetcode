import collections
from typing import List

class Solution:
    def relativeSortArray0(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = {num:idx for idx, num in enumerate(arr2)}
        return(sorted(arr1, key=lambda a: k.get(a, 1000+a)))
        # arr1.sort(key=lambda x: arr2_dict[x] if x in arr2_dict else 1001 + x)

#you are sorting initial list A with key function that will get index of element in A 
#from hashmap that you already created and in case it's not there it will add 1000 to 
#the element itself so it will put elements that are in A but not in B after all the 
#elements in resulting list. 

    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # collections.counter then pop the count based on element
        ans, cnt = [], collections.Counter(arr1)         # Count each number in arr1
        print(cnt)
        for i in arr2:
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the common numbers in both arrays by the order of arr2. 
        for i in range(1001):                            # For numbers still in arr1
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the numbers only in arr1.
            print(cnt, ans)
        return ans

    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = []
        r = []
        m = {} # count

        # initialize counts for elements in arr2
        for num in arr2:
            if num not in m:
                m[num] = 0

        for num in arr1:
            if num in m:
                m[num] += 1
            else:
                diff.append(num)

        diff.sort()

        for num in arr2:
            r.extend([num] * m[num]) 

        r.extend(diff)

        return r 

    def relativeSortArray3(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        li_dif=[n for n in arr1 if n not in arr2]
        li_dif.sort()

        res = []
        arr1_cnt = collections.Counter(arr1)
        for n in arr2:
            res =res+ [n] * arr1_cnt[n]
        
        res=res+li_dif
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.relativeSortArray0([2,3,1,3,2,4,6,19,9,2,7],[2,1,4,3,9,6]))
    print(s.relativeSortArray1([2,3,1,3,2,4,6,19,9,2,7],[2,1,4,3,9,6]))
    print(s.relativeSortArray2([2,3,1,3,2,4,6,19,9,2,7],[2,1,4,3,9,6]))
    print(s.relativeSortArray3([2,3,1,3,2,4,6,19,9,2,7],[2,1,4,3,9,6]))


