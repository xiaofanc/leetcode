"""
You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array damage where damage[i] is the amount of health you will lose to complete the ith level.

You are also given an integer armor. You may use your armor ability at most once during the game on any level which will protect you from at most armor damage.

You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

Return the minimum health you need to start with to beat the game.
"""

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # get the min and max damage and sum damage
        mind, maxd, sumd = float("inf"), float("-inf"), 0
        for d in damage:
            mind = min(mind, d)
            maxd = max(maxd, d)
            sumd += d
        # if armor < min damage, does not matter when to use the armor
        # minhealth = sum-armor+1
        if armor < mind:
            minhealth = sumd - armor + 1
        # if armor > max damage, use the armor for the max damage
        # minhealth = sum-max+1
        elif armor > maxd:
            minhealth = sumd - maxd + 1
        # else, use the armor for the max damage or damage >= armor
        # minhealth = sum-max+(max-armor)+1
        else:
            minhealth = sumd - maxd + (maxd - armor) + 1
        return minhealth

    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) - min(armor, max(damage)) + 1
        
if __name__ == '__main__':
    s = Solution()
    print(s.minimumHealth([2,7,4,3], 4))


