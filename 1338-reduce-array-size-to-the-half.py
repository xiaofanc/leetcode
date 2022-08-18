

class Solution:
	# Time: O(n)
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        n = len(arr)
        bucket = [[] for _ in range(n+1)]
        for k, freq in count.items():
            bucket[freq].append(k)
        
        # print("bucket->", bucket)
        cnt = 0
        left = n
        for i in range(n,0,-1):
            for num in bucket[i]:
                cnt += 1
                # print("i, cnt", i, cnt)
                left = left - i
                if left <= n//2:
                    return cnt

    # Time: O(nlogn)
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        n = len(arr)
        cnt = 0
        left = n
        
        for k, v in sorted(count.items(), key=lambda item: -item[1]):
            cnt += 1
            left -= v
            if left <= n//2:
                return cnt

if __name__ == '__main__':
	s = Solution()
	print(s.minSetSize([3,3,3,3,5,5,5,2,2,7])) # 2
                    
        
