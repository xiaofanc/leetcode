def get_different_number(arr):
  # solution 1: sorting the arr and loop over the sorted arr (Time: O(nlogn+n0))
  # solution 2: put the numbers from the arr into a set, loop starting from 0
  #             if num is not set, return num (Time: O(n), Space: O(N))
  #             [10, 11, 12] --> 0 
  # https://www.linkedin.com/in/eugenesha/
  if not arr:
    return 0
  num = set(arr)
  
  # [0, 1, 2, 3, 4]
  n = len(arr)
  for i in range(n):
    if i not in num:
      return i
  return n