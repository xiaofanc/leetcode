class Solution:

    # Time: O(n^2), space: O(n)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # The smaller persons are "invisible" for the taller ones, and hence one could first arrange the tallest guys as if there was no one else.
        # sort people by height descending
        # if height is the same, sort by each guy's k value, ascending
        # each guy's index is equal to his k value
        people.sort(key = lambda x: (-x[0], x[1]))
        # print(people)
        output = []
        for p in people:
            output.insert(p[1], p) # up to O(k) time, k is the # element in the list
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])) # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]