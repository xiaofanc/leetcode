def flip(arr, k):
  # arr = [1,2,3,4], k = 2
  # output = [2,1,3,4]
  l, r = 0, k-1
  while l < r:
    arr[r], arr[l] = arr[l], arr[r]
    l += 1
    r -= 1
  #return arr
  
 # [ 4, 4, 4 ,9, ]
  # 
def helper(arr): 
  # find the index of the largest number
  n, idx = float('-inf'), 0
  for i, v in enumerate(arr):
    if v > n:
      idx = i
      n = v
  return idx

#linpatrick11@gmail.com
#https://www.linkedin.com/in/pl728/
  
def pancake_sort(arr):
  # [1,5,4,3,2] 
  # flip([1,5,4],3) -> [..,5]
  # how to flip to move the larger num to the end?
  # loop over the arr 
  # when I reach the number that I want to flip -> 5 (k=1)
  # first I flip(arr, k=2) -> [5,1,4,3,2]
  # second I flip(arr, k=len(arr)) -> [2,3,4,1,5]
  # then I want to find 4 in the [2,3,4,1,5] -> 4 (k=2)
  # then I flip(arr, k=3) -> [4,3,2,1,5]
  # flip the arr -> [1,2,3,4,5] 
  # early stop 
  n = len(arr)
  count = 0
  while count < n:
    # return the position of the number that we want to put for the next position
    idx = helper(arr[:n-count]) 
    # we flip to move the target to the right position
    # flip to move the number that we want to the index = 0
    flip(arr, idx+1)   # [5,1,4,3,2]
    # flip to move the number from index = 0 to the position that we want
    flip(arr, n-count) # [2,3,4,1,5]
    # we continue to search the next number
    count += 1
  return arr

# print(pancake_sort( [1, 5, 4, 3, 2]))
    
    
    
    
   