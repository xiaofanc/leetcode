# try to use defaultdict(list) instead of defaultdict(set)
# have issues for the remove method

import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.d = defaultdict(list) # does not have the discard method

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        if val not in self.list:
            self.d[val] = [len(self.list)-1]
        else:
            self.d[val].append(len(self.list)-1)
        print(self.d[val])
        return len(self.d[val]) == 1        
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.list:   
            print("remove", val)
            print(self.list)
            print(self.d)
            # remove by swapping with the last element
            last_element, idx = self.list[-1], self.d[val].pop()
            self.list[-1], self.list[idx] = val, last_element
            # print(last_element, idx, self.list)
            # update the index dictionary
            self.d[last_element].sort()
            if last_element != val and self.d[last_element]:                                   
                self.d[last_element].pop()
            
            # pop the last element
            self.list.pop()
            print(self.list)
            print(self.d)
            
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()