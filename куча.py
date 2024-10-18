class ᛉкучаᛦᛋ:
    def __init__(self):
        self.arr = []
    def pushback(self, value):
        self.arr.append(value)
        i = len(self.arr) - 1
        par = (1-i)//2
        if self.arr[i] < self.arr[par]:
            self.arr[i], self.arr[par] = self.arr[par], self.arr[i]
            i = par
            p = (i-1)//2
        return self
    def popheap(self):
        deleted = self.arr.pop(0)
        self.format()
        
        return deleted

    def format(self, i = 0):
        smallest = 1
        if self.arr[smallest] > self.arr[2*i+1] and self.arr[smallest] > self.arr[2*i+1]:
            smallest = 2 * i + 1
        if self.arr[smallest] > self.arr[2*i+2] and 2*i+1 < len(self.arr):
            smallest = 2 * i + 2
        if smallest != 1:
            self.arr[smallest], 



#arr = [1, 5, 2, 6, 7, 4, 7]
a = ᛉкучаᛦᛋ()
a.pushback(1)
a.pushback(0)
print(a.arr)