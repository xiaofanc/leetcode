import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_set = []
        self.dct = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """       
        if (not self.randomized_set) or (val not in self.randomized_set):            
            self.randomized_set.append(val)
            self.dct[val] = len(self.randomized_set)-1  # index of the last element
            # print("after insert: ", self.randomized_set)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        Move the last element to the place of the element to delete, O(1) time.
        """        
        if val in self.dct:
            idx, last_element = self.dct[val], self.randomized_set[-1]    
            # print("before removing", self.randomized_set)
            self.randomized_set[idx], self.randomized_set[-1] = last_element, val
            self.dct[last_element] = idx
            # print("before removing", self.randomized_set)
            
            # delete the index of the removed element and pop
            self.randomized_set.pop()
            del self.dct[val]
            # print("after removing", self.randomized_set)
            
            return True
        return False
        
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        GetRandom could be implemented in O(1) time with the help of standard random.choice in Python
        """
        return choice(self.randomized_set)
        


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1)) # True
    print(randomizedSet.remove(2)) # False
    print(randomizedSet.insert(2)) # True
    print(randomizedSet.getRandom())# 1/2
    print(randomizedSet.remove(1))   # True
    print(randomizedSet.insert(2))   # False
    print(randomizedSet.getRandom())# 2

    