class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # for each letter encountered, process the last occurrence of that letter
        # extend the current partition [anchor, j] appropriately
        
        # find the last occurrence
        last = {c: i for i, c in enumerate(s)}

        anchor = j = 0
        res = []
        for i, c in enumerate(s):
            # update the end of the partition by the last occurrence of c
            j = max(j, last[c])
            if i == j:
                # end of the partition
                res.append(j - anchor + 1)
                # new start of the next partition
                anchor = i + 1
        return res
            

    def partitionLabels(self, s: str) -> List[int]:
        # remember the start and the end of each letter
        # merge the overlapping intervals
        occurrence = {}
        # sort by the start of each letter
        str_occur = []
        for i in range(len(s)):
            if s[i] not in occurrence:
                occurrence[s[i]] = [i]
                # remember the order of the letter that occurred
                str_occur.append(s[i])
            else:
                occurrence[s[i]].append(i)
        
        # start and end of the partition
        start, end = 0, 0
        res = []
        for letter in str_occur:
            if occurrence[letter][0] <= end:
                end = max(end, occurrence[letter][-1])
            else:
                res.append(end - start + 1)
                start = occurrence[letter][0]
                end = occurrence[letter][-1]
        res.append(end - start + 1)    
        return res  

if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
    print(s.partitionLabels("eccbbbbdec")) # [10]





