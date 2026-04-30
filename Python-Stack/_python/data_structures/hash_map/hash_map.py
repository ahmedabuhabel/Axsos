class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        id = self._hash(key)
        for item in self.table[id]:
            if item[0] == key:
                item[1] = value
                return
        self.table[id].append([key, value])

    def get(self, key: int) -> int:
        id = self._hash(key)
        for item in self.table[id]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        id = self._hash(key)
        for i, item in enumerate(self.table[id]):
            if item[0] == key:
                del self.table[id][i]
                return
