class MyHashSet:
    def __init__(self):
        self.st = set()

    def add(self, key: int) -> None:
        self.st.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.st.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.st:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)