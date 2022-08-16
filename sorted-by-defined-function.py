class Solution:
    def reorderLogFiles(self, logs) :
        def f(log):
            id_, tail = log.split(" ", 1) 
            print(id_)
            print(tail)
            print(log)
            return (0, tail, id_) if tail[0].isalpha() else (1,)
            
        return sorted(logs, key=f)


def f(a, b):
  if abs(a) > abs(b): return 1
  if abs(a) < abs(b): return -1
  if a > b: return 1
  if a < b: return -1
  return 0

def absSort(arr):
  # check if abs(arr[i+1]) == abs(arr[i])
  # if same, then If arr[i+1] < 0 and arr[i] > 0: then swap
  # arr.sort(key = compare)
  return sorted(arr, cmp=lambda x, y: f(x, y))
  