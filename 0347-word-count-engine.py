import collections
def word_count_engine(arr):
  '''
  input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

  output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
  O(nlogn) using sort
  
  N => length of words in document
  
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
  [[] [makes, youll, only.... ], [perfect] , [practice],                        []    ]
  
  '''
  l, r = 0, 0
  # OrderedDict to keep the order !!!
  count = collections.OrderedDict()
  # remove the left empty space
  arr = arr.strip()
  word = ""
  cnt = 1
  while r < len(arr):
    if arr[r].isalpha(): 
      word += arr[r]
      r += 1
    elif arr[r] == " ":
      cnt += 1
      count[word.lower()] = count.get(word.lower(), 0) + 1
      word = ""
      while arr[r] == " ":
        r += 1
      l = r # move to the next word
    else:
      r += 1
      
  count[word.lower()] = count.get(word.lower(), 0) + 1
  #print("count->", count)
  
  # create the freq bucket
  # bucket sort - O(n)
  bucket = [[] for i in range(cnt)]
  for k, v in count.items():
    bucket[v].append(k)
  
  res = []
  for i in range(cnt-1,0,-1):
    for j in range(len(bucket[i])):
      res.append([bucket[i][j], str(i)])
  #print("res->", res)
  return res
      
  
print(word_count_engine("      Practice makes perfect.     you'll only get Perfect by practice. just practice!"))

      
      
    
      
  
  