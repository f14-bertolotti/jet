class Counter():
    def __init__(self, max=None): 
        self.count, self.max = 0, max
    def __iter__(self):
        while True:
            self.count += 1
            if self.max and self.count >= self.max: raise StopIteration
            yield self.count
