"""
Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""
class TimeMap:

    def __init__(self):
        self.dct = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # override
        self.dct[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dct:
            for t in range(timestamp,-1,-1):
                if t in self.dct[key]:
                    return self.dct[key][t]
        # if key does not exist
        return ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

