# arr = ["perfect", "makes", "practice"]
# output = ["practice", "makes", "perfect"]
# word = ["p", "e", .."t"], [], []
# res = [" ","p", "e", .."t"]
# case 2: ["a"," "," ","b"]

def reverse_words(arr):
  def helper(i, j):
    while i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1
    
  # reverse array
  helper(0, len(arr)-1)
  # reverse each word
  left = 0
  n = len(arr)
  for i, char in enumerate(arr):
    if char == " ":
      helper(left, i-1)
      left = i+1
      while left < n-1 and arr[left] == " ":
        left += 1
  helper(left, len(arr)-1)
  return arr

print(reverse_words([" ", "a", "v"," "," ", "b", "u"])) # ['b', 'u', ' ', ' ', 'a', 'v', ' ']
        
        
      
    
      
      
      
  


