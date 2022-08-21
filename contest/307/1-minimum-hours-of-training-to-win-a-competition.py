

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        E = 1 + sum(energy) - initialEnergy
        exp = initialExperience
        T = 0
        for i in range(len(experience)):
            if exp > experience[i]:
                exp += experience[i]
            else:
                while exp <= experience[i]:
                    exp += 1
                    T += 1
                exp += experience[i]
        # print(E, T)
        return max(0, E) + T
            
            