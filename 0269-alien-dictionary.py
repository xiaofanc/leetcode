class Solution:
    def alienOrder(self, words: List[str]) -> str:
        less = []
        for pair in zip(words, words[1:]):
            #print(*pair)
            for a, b in zip(*pair):
                # compare the first different str
                if a != b:
                    less.append(a+b)
                    #print(less)
                    break
        chars = set("".join(words))
        print('less', less, 'chars', chars)
        order = []
        while less:
            print('chars',chars, list(zip(*less))[1])
            #free is the char that does not have pointer
            free = chars - set(list(zip(*less))[1])
            print("free", free)
            if not free:
                return ""
            order += free
            #delete char with free as the first char from less
            less = list(filter(free.isdisjoint, less))
            print('less', less, 'order', order)
            chars -= free
        return "".join(order + list(chars))
                
if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
