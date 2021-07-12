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
                f[ID]+= timespent
                print(f)
                #remove the overlapping time 
                
                if stack:
                    f[stack[-1][0]]-= timespent
                    print(f)
                    
        return f

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [] # only store the start time
        res = [0]*n
        for log in logs:
            taskid, session, time = log.split(":")
            taskid = int(taskid)
            time = int(time)
            if session == "start":
                stack.append([taskid, time])
                print('stack:', stack)
            else: # session == "end"
                # single-threaded, it looks like one task will be interrupted by other tasks
                # therefore, prev_id = taskid
                prev_id, prev_time = stack.pop()
                res[taskid] += time - prev_time + 1
                overlap = time - prev_time + 1 
                print('stack:', stack)
                print(res)
                
                # remove the overlapping time from the preivous ongoing task
                # ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
                # In this case, time for "0:start:2","0:end:5" = 4
                # remove 4 from previous -> same task, so it is cancelled
                if stack:
                    # store the time that needs to be removed from the task due to overlapping
                    # "0:start:2","0:end:5" does not remove any time for the task 0
                    res[stack[-1][0]] -= overlap
                    print("remove overlap", res)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])) #[7,1]
    print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])) #[3,4]







