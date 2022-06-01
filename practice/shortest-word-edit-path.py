"""
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

BFS:
method 1:
for every index i from 0 .. word.length - 1 and for every lowercase letter c in ['a-z'], copy word into word2, replace word2[i] with c, and check whether the resulting word2 is in words.

method 2:
for every word2 in the given words, check that word and word2 differ by 1. If diff = 1, then add to the Queue

Queue: [(bit, 0)]
       pop bit, append word which has one character different from bit
       [(but, 1), (big, 1)]
       pop but, append word which has one character different from but
       [(big, 1), (put, 2)]
       pop big, append word which has one character ....... big
       [(put, 2)]
       pop put...
"""

# Time complexity: N*K^2 where N is the length of words and K is the maximum length of any given word.
# Space complexity: NK
from collections import deque
def shortestWordEditPath1(source, target, words):
    queue = deque()
    queue.append((source, 0))
    seen = set()
    wordset = set(words)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while queue:
        word, depth = queue.popleft()
        if word == target:
            return depth
        for i in range(len(word)):
            for c in alphabet: # change one char in word
                word2 = list(word)
                word2[i] = c
                word2 = "".join(word2)
                if word2 in wordset and word2 not in seen:
                    queue.append((word2, depth+1))
                    seen.add(word2)
                    print("queue", queue)
    return -1

def shortestWordEditPath2(source, target, words):
    """
    @param source: str
    @param target: str
    @param words: str[]
    @return: int
    """
    queue = deque()
    queue.append((source, 0))
    seen = set()
    wordset = set(words)

    while queue: # K?
        word, depth = queue.popleft()
        if word == target:
            return depth
        for word2 in wordset: # N
            if len(word2) == len(word):
                # diff = len(set(word2) - set(word)) - does not work for 'aa', 'bb'
                diff = 0
                for i in range(len(word2)):  # K
                    if word[i] != word2[i]:
                        diff += 1
                if diff == 1 and word2 not in seen:
                    queue.append((word2, depth+1))
                    seen.add(word2)

    return -1

from collections import defaultdict

def shortestWordEditPath3(source, target, words):
  
  def getAllPerms(w):
    perms = []
    wl = list(w)
    for i in range(len(w)):
      wlclone = wl[:]
      wlclone[i] = '#'
      perms.append(''.join(wlclone))
    return perms
  
  # preprocessing words
  wdict = defaultdict(list)
  for w in words:
    perms = getAllPerms(w)
    print("w, perms->", w, perms)
    for k in perms:
      wdict[k].append(w)
    print("wdict->", wdict)
    
  visited = set()
  visited.add(source)
  queue = [(source, 0)]
  
  while queue:
    word, dist = queue.pop(0)
    if word == target:
      return dist
    perms = getAllPerms(word)
    print("check->", word, perms)
    # find the words with one character difference
    for p in perms:
      nwords = wdict[p]
      for word in nwords:
        if word not in visited:
          visited.add(word)
          queue.append((word, dist+1))
          print('queue', queue)
    
  return -1

# print(shortestWordEditPath1("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]))   # 5 bit -> but -> put -> pot -> pog -> dog
# print(shortestWordEditPath2("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]))   # 5 
# print(shortestWordEditPath2("no", "go", ["to"]))   # -1
# print(shortestWordEditPath2("no", "ge", ["ne", "po", "ge"]))   # 2
print(shortestWordEditPath3("aa", "bb", ["ab", "bb"]))   # 2
	

  