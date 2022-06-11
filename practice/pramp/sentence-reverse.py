"""
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
		'm', 'a', 'k', 'e', 's', '  ',
		'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
	  'm', 'a', 'k', 'e', 's', '  ',
	  'p', 'e', 'r', 'f', 'e', 'c', 't' ]
"""

# arr = ["perfect", "makes", "practice"]
# output = ["practice", "makes", "perfect"]
# case 2: ["a"," "," ","b"]


class Solution:
    def reverse_words(arr):
        # no need to pass/return arr
        def helper(i, j):
	        while i < j:
	            arr[i], arr[j] = arr[j], arr[i]
	            i += 1
	            j -= 1

        # reverse array
        helper(0, len(arr)-1)

        # reverse each word
        left, n = 0, len(arr)
        for i, char in enumerate(arr):
        if char == " ":
            helper(left, i-1)
            # move left to the next word
            left = i+1
            while left < n and arr[left] == " ":
            	left += 1

        # reverse the final part!
        helper(left, len(arr)-1)
        return arr

    def reverse_words(arr):
        word = []
        res = [" "] * len(arr)
        second = len(res)-1
        for i in range(len(arr)):
        if arr[i] != " ":
            word.append(arr[i])
        # the last char does not have " " in the end
        if arr[i] == " " or i == len(arr)-1:
            # add the word to the res
            first = len(word)-1
            while first >= 0:
	            res[second] = word[first]
	            second -= 1
	            first -= 1
	        second -= 1
	        word = []
        return res

    def reverse_words(arr):
        def helper(i, j):
	        while i < j:
	            arr[i], arr[j] = arr[j], arr[i]
	            i += 1
	            j -= 1

        # reverse array
        helper(0, len(arr)-1)
        # reverse each word
        wordstart = 0
        n = len(arr)
        for i in range(n):
        if arr[i] == " ":
            helper(wordstart, i-1)
        	wordstart = i+1
            while arr[wordstart] == " " and wordstart < n-1:
                wordstart += 1
        elif i == n-1:
            helper(wordstart, i)
        return arr
