"""
["0:start:0","1:start:2","0:end:5"] will not happen since 2 tasks cannot run at the same time
The total exclusive time of all tasks should add up to end(last)-start(first)+1

["0:start:0","1:start:2","2:start:4","2:end:4","1:end:5","0:end:6"]
remove the overlapping time:
execution time of task 2: 1
remove the execution time of task 2 (total time: 1) from task 1 (4): 4-1=3
remove the execution time of task 1 (total time: 4) from task 0 (7): 7-4=3
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        f = [0]*(n)
        stack=[]
              
        for i in logs:
            
            ID,pos,time = i.split(':')
            
            ID= int(ID)
            time= int(time)
            if pos == 'start':                
                stack.append([ID,time])
                print('stack: ', stack)
            else:                
                prID, prtime = stack.pop()                
                timespent = time-prtime+1
                f[ID]+= timespent  # same as prID
                print(f)
                #remove the overlapping time 
                
                if stack:
                    f[stack[-1][0]]-= timespent
                    print(f)
                    
        return f

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        # start time of the current task on the CPU
        prev_time = 0 
        for log in logs:
            fid, p, t = int(log.split(":")[0]), log.split(":")[1], int(log.split(":")[2])
            if p == "start":
                if stack:
                    # add time for previous task
                    res[stack[-1]] += t-prev_time
                stack.append(fid)
                prev_time = t
            else:
                # calculate time for the task which ended
                res[stack.pop()] +=t-prev_time+1
                # restart the previous task
                prev_time = t+1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])) #[7,1]
    print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])) #[3,4]







