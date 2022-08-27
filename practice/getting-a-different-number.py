def get_different_number(arr):
  # solution 1: sorting the arr and loop over the sorted arr (Time: O(nlogn+n))
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

# solution 3:
# arr must contain [0...n-1]
# cyclic replacement to move num into their corrent position
def get_different_number(arr): # arr = [1,0,3,4,5]
  if not arr:
    return 0
  n = len(arr)
  
  for i in range(n):
    # update tmp to be the next num
    tmp = arr[i]   
    while tmp < n and tmp != arr[tmp]:
      arr[tmp], tmp = tmp, arr[tmp]
  #print("arr->", arr) [0,1,3,3,4]
  for i in range(n):
    if arr[i] != i:
      return i
  return n

print(get_different_number([0])) # 1
print(get_different_number([0,1,2])) # 3
print(get_different_number([6,7,8])) # 0
print(get_different_number([1,0,3,4,5])) # 2



