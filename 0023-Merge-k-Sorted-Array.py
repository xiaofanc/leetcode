import heapq
from heapq import heapify, heappop, heappush

class Solution:
    def merge(self, arrays):
        """
        input: int[][] arrays
        return: int[]
        """
        # write your solution here
        heap=[]
        for i in range(len(arrays)):
            if len(arrays[i]):
                heap.append((arrays[i][0],i,0))    # each node has three values
        heapq.heapify(heap)
        result=[]
        while heap:
            val, index_array, index_element = heapq.heappop(heap)
            result.append(val)
            if index_element + 1 < len(arrays[index_array]):
                heapq.heappush(heap,(arrays[index_array][index_element + 1],index_array, 
                index_element+1))
        return result    

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,2,5],[2,5,7],[3,4]]))