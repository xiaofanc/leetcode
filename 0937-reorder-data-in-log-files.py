class Solution:
    def reorderLogFiles(self, logs) :
        def f(log):
            id_, tail = log.split(" ", 1) 
            print(id_)
            print(tail)
            print(log)
            return (0, tail, id_) if tail[0].isalpha() else (1,)
            
        return sorted(logs, key=f)

s=Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(s.reorderLogFiles(logs))