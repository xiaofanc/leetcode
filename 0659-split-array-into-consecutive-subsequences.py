

class Solution:
	# 41 / 187 test cases passed.
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        visited = [False]*len(nums)
        
        def backtrack(i, comb):
            if len(comb) >= 3: # does not continue if subsets > 3; [1,2,3,4,4,5]
                res.append(comb[:])
                return backtrack(0, [])
            if i == len(nums):
                return True
            for j in range(i, len(nums)):
                if visited[j]:
                    continue
                if not comb or nums[j] == comb[-1]+1:
                    visited[j] = True
                    comb.append(nums[j])
                    if backtrack(j+1, comb):
                        return True
                    comb.pop()
                    visited[j] = False
            return False
        
        return backtrack(0, [])

    # greedy using heap: O(NlogN)
    # find the shortest subsequence where we can append nums[i]
    def isPossible(self, nums: List[int]) -> bool:
        """
        use a heap to store the first and last element of each subsequence in the array
            - first sort by the last element
            - second sort by length
        iterate over nums
            - compare the last element of existing subsequence in the heap with num. If the last element is smaller than num-1, we cannot add num or any future elements to the subsequence, remove it from the heap. While removing, check if length is >= 3, if not, return False
            - if the heap is empty or the last element of the first subsequence in the heap is equal to num, create a new subsequence with num and add to the heap
            - if there exists valid subsequences, add num to the subsequence with smaller length

        check the length of all subsequences in the heap, if any length < 3: return False
        """
        heap = [] # (last, length, first)
        for num in nums:
            # condition-1: remove non qualifying subsequences
            while heap and heap[0][0] < num-1:
                subseq = heapq.heappop(heap)
                if subseq[1] < 3:
                    return False
            # condition-2: heap is empty or last of the first subseq == num
            if not heap or heap[0][0] >= num:
                subseq = (num, 1, num)
                heapq.heappush(heap, subseq)
            else: # condition-3: heap is not empty and last == num-1, the first subseq is smaller
                subseq = heapq.heappop(heap)
                newseq = (num, subseq[1]+1, subseq[2])
                heapq.heappush(heap, newseq)
        while heap:
            if heapq.heappop(heap)[1] < 3:
                return False
        return True


    def isPossible(self, nums: List[int]) -> bool:
        """
        Initialize two maps - one to store the frequency of each element present in nums array (frequency), the other to store the frequency of subsequences ending with the key.
        loop over the num and update the frequency map
        loop over the num
            - if freq[num] == 0: it is already considered to be part of a valid subseq
            - check if subseq[num-1] exists, if yes, it means we can add num to an existing subsequence, update subseq map
            - if no such subsequence exists, we need to create a new subsequence with num and check if num+1, num+2 exist or not.
        return True
        """
        freq = collections.Counter(nums)
        subseq = defaultdict(lambda: 0) # count the last element of subsequences
        for num in nums:
            # condition-1: num is already in the subseq
            if freq[num] == 0:
                continue
            # condition-2: check if we can append num into valid subseq
            elif subseq[num-1] > 0:
                subseq[num-1] -= 1
                subseq[num] += 1
            # condition-3: no valid subseq to append, create a new one
            else:
                if freq[num+1] > 0 and freq[num+2] > 0:
                    freq[num+1] -= 1
                    freq[num+2] -= 1
                    subseq[num+2] += 1
                else:
                    return False
            freq[num] -= 1
        return True



        
