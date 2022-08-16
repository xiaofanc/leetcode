def absSort(arr):
  # check if abs(arr[i+1]) == abs(arr[i])
  # if same, then If arr[i+1] < 0 and arr[i] > 0: then swap
  arr = sorted(arr, key = lambda x: abs(x))
  for i in range(len(arr)-1):
    if abs(arr[i+1]) == abs(arr[i]):
      if arr[i+1] < 0 and arr[i] > 0:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr
	
#solution 2:
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
  
