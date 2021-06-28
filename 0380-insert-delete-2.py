import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_set = []
        self.dct = {}
        self.size = -1
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """       
        if (not self.randomized_set) or (val not in self.randomized_set):            
            self.randomized_set.append(val)
            self.size += 1
            self.dct[val] = self.size  # index of the last element
            # print("after insert: ", self.randomized_set)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """        
        if val in self.randomized_set:
            idx = self.dct[val]
            # print("swap: ", idx)
            # swap with the last element
            # print("before remove: ", self.randomized_set)
            temp = self.randomized_set[-1]
            self.randomized_set[idx] = temp
            self.randomized_set[-1] = val
            
            # update the index of the swapping elements in the dictionary
            # update the index of the previous last element
            self.dct[self.randomized_set[idx]] = idx
            # delete the index of the remove element
            del self.dct[val]
            # update the size
            self.size -= 1
            
            self.randomized_set.pop()
            # print("after remove: ", self.randomized_set)
            return True
        else:
            return False
        
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.randomized_set)-1)
        return self.randomized_set[idx]
        


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1)) # True
    print(randomizedSet.remove(2)) # False
    print(randomizedSet.insert(2)) # True
    print(randomizedSet.getRandom())# 1/2
    print(randomizedSet.remove(1))   # True
    print(randomizedSet.insert(2))   # False
    print(randomizedSet.getRandom())# 2



    