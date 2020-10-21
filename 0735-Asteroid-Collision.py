from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack
        # when it will collide: asteroids[i] > 0 > asteroids[i+1]
        res = []
        for new in asteroids:
            while res and res[-1] > 0 > new:
                if res[-1] == -new: # [8, -8]
                    res.pop()
                    break # jump to the for-loop
                elif res[-1] < -new: # [3, -5]
                    # collide
                    res.pop()
                    continue # jump to the while-loop
                else: # [10,-3]
                    break # jump to the for-loop
            # other conditions will not collide
            else: 
                res.append(new)
        return res
                    
                    
                
if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([5,10,-5]) == [5,10])
    print(s.asteroidCollision([8,-8]) == [])
    print(s.asteroidCollision([-2,-1,1,2]) == [-2,-1,1,2])
    print(s.asteroidCollision([10,2,-5]) == [10])