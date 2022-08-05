
# case 1: when M is similar to N
def find_duplicates(arr1, arr2):
  # Time: O(M) + O(N)
  res = []
  p1, p2 = 0, 0
  while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] < arr2[p2]:
      p1 += 1
    elif arr1[p1] == arr2[p2]:
      res.append(arr1[p1])
      p1 += 1
      p2 += 1
    else:
      p2 += 1
  return res  

# case 2: when N >> M        
def find_duplicates(arr1, arr2):
  '''
  arr1[1, 3, ^31-1] m=2
  arr2[4,6...2^31]  n=200k
  '''
  # Time: O(MlogN), where N is the longer array
  res = []
  # arr1 is the longer array
  if len(arr2) > len(arr1):
    arr1, arr2 = arr2, arr1
    
  for n in arr2:   # mlogn ? m+n
    # binary search the longer array arr1
    l, r = 0, len(arr1)-1
    while l <= r:
      m = l + (r-l)//2
      if arr1[m] == n:
        res.append(n)
        break
      elif arr1[m] > n:
        # search the left part
        r = m-1
      else:
        l = m+1
  return res
        
print(find_duplicates([1,2,3,5,6,7], [3,6,7,8]))
  