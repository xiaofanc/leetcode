class Solution:
    def reorderLogFiles(self, logs) :
        def f(log):
            id_, tail = log.split(" ", 1) 
            print(id_)
            print(tail)
            print(log)
            return (0, tail, id_) if tail[0].isalpha() else (1,)
            
        return sorted(logs, key=f)