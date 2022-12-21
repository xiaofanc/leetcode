class TwoSum:

    def __init__(self):
        self.freq = dict()

    def add(self, number: int) -> None:
        self.freq[number] = self.freq.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for k, v in self.freq.items():
            other = value-k
            if other == k and v > 1:
                return True
            elif other != k and other in self.freq:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)