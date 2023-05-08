from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.n2f = dict()
        self.f2n = defaultdict(set)

    def add(self, number: int) -> None:
        self.n2f[number] = self.n2f.get(number, 0) + 1
        freq = self.n2f[number]
        if freq == 1:
            self.f2n[freq].add(number)
        else:
            self.f2n[freq-1].remove(number)
            self.f2n[freq].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.n2f:
            self.n2f[number] -= 1
            freq = self.n2f[number]
            self.f2n[freq+1].remove(number)
            if freq > 0:
                self.f2n[freq].add(number)
            elif freq == 0:
                del self.n2f[number]

    def hasFrequency(self, frequency: int) -> bool:
        if len(self.f2n[frequency]) > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)


