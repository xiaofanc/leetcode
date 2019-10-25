class MyHashMap:

    def __init__(self):
        self.lst = list()
        

    def put(self, key: int, value: int) -> None:
        self.lst.append((key,value))

    def get(self, key: int) -> int:
        ans = -1
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
                ans = self.lst[i][1]
        return ans

            
    def remove(self, key: int) -> None:
        self.lst.append((key, -1))

if __name__ == '__main__':
    m = MyHashMap()
    print(m.put(1,1))
    print(m.put(2,2))
    print(m.get(1))
    print(m.get(3))
    print(m.put(2,1))
    print(m.get(2))
    print(m.remove(2))
    print(m.get(2))









