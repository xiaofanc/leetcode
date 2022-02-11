"""
OrderedDict in python is implemented by a dict+linkedList, which is essentially a LRU cache.
"keyfreq" dict represents a normal dict that maps one key to one frequency.
"freqkeys" dict represents a dict that maps one freq to many keys, and these "many keys" are stored in OrderedDict.
With this two dicts, given one key, we can find its frequency, and with its frequency, we can find all other keys of the same frequency.
When there are many items of same frequency, the OrderedDict in freqkeys dict correctly records the item order in LRC fashion where the first item will be the one to pop out.

https://leetcode.com/problems/lfu-cache/discuss/166683/Python-only-use-OrderedDict-get-O(1)-put-O(1)-Simple-and-Brief-Explained!!!!!!

https://leetcode.com/problems/lfu-cache/discuss/369104/Python-two-dicts-explanation

"""

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.minfreq=None
        self.keyfreq={}
        # LRU must be used in case delete keys with same freq
        self.freqkeys=collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyfreq:
            return -1
        freq=self.keyfreq[key]
        val=self.freqkeys[freq][key]
        
        # update the dictionary since freq now +1
        del self.freqkeys[freq][key]
        
        # if key is the only one with the minfreq
        if not self.freqkeys[freq] and freq==self.minfreq: 
            self.minfreq+=1
            del self.freqkeys[freq]
            
        self.keyfreq[key]=freq+1
        self.freqkeys[freq+1][key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0:
            return
        # update if key exists
        if key in self.keyfreq:
            freq=self.keyfreq[key]
            self.freqkeys[freq][key]=value
            self.get(key) # update frequency
            return

        if self.capacity==len(self.keyfreq):
            # get the LRU key with minfreq
            delkey, delval=self.freqkeys[self.minfreq].popitem(last=False)
            del self.keyfreq[delkey]

        # insert the key-value pair
        self.keyfreq[key]=1
        self.freqkeys[1][key]=value
        self.minfreq=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
