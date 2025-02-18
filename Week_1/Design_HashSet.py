# class MyHashSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
        

#     def add(self, key: int) -> None:
        

#     def remove(self, key: int) -> None:
        

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
        


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]