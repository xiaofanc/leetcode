
def deletion_distance(str1, str2):

  def dfs(i, j):
    remove = 0
    # calculate min chars to remove for str1[i:] and str2[j:]
    if i == len(str1) and j == len(str2):
      return 0
    if i == len(str1) and j != len(str2):
      return len(str2[j:])
    if j == len(str2) and i != len(str1):
      return len(str1[i:])
    # when i < len(str1) and j < len(str2)
    if str1[i] == str2[j]:
      remove += dfs(i+1, j+1)
    else:
      remove += min(1+dfs(i+1, j), 1+dfs(i, j+1,), 2+dfs(i+1, j+1))
    
    return remove
  
  return dfs(0, 0)


def deletion_distance(str1, str2):
  
  m, n = len(str1), len(str2)
  dp = [[0]*(m+1) for _ in range(n+1)]
  for i in range(n+1):
    dp[i][m] = len(str2[i:])
  for j in range(m+1):
    dp[n][j] = len(str1[j:])
  
  for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
      if str2[i] == str1[j]:
        dp[i][j] = dp[i+1][j+1]
      else:
        dp[i][j] = min(1+dp[i+1][j], 1+dp[i][j+1], 2+dp[i+1][j+1])
  return dp[0][0]    

print(deletion_distance("dog", "frog")) # 3
print(deletion_distance("", "")) # 0


