
def flatten_dictionary(dictionary):
  # dfs(prev, dictionary), prev to record previous key
  # loop over the key, value pair in the dict
  # base case: if the value for the dict is not a nested dict then add to the res
  # else call dfs in the value so that we can add the nested pairs
  res = {} 
  def dfs(prev, dictionary):  # if prev == "" or key == ""
    for key, val in dictionary.items():
      if prev != "":
        newKey = prev + '.' + key if key else prev
      else:
        newKey = key if key else prev
        
      if type(val) is dict:
        dfs(newKey, val)
      else:
        res[newKey] = val
      
  dfs("", dictionary)
  return res
  
  # "Key2.c.e" : "1 != "Key2.c.e." : "1

dct = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

print(flatten_dictionary(dct)) # {'Key1': '1', 'Key2.a': '2', 'Key2.b': '3', 'Key2.c.d': '3', 'Key2.c.e': '1'}
