"""
given an almost sorted array in which each number is less than m spots away from its correct sorted position and the value m.
return a proper sorted array.

"""
import heapq

def sort_list(almost_sorted_list, m):
    min_heap, result = [], []
    for elem in almost_sorted_list[:m]:
        heapq.heappush(min_heap, elem)

    for elem in almost_sorted_list[m:]:
        heapq.heappush(min_heap, elem)
        result.append(heapq.heappop(min_heap))

    for i in range(len(min_heap)):
        result.append(heapq.heappop(min_heap))

    return result

print(sort_list([3,4,1,2,6,5], 3))