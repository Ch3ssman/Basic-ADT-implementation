class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
    def __str__(self):
        return str(self.binary_heap)
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0 
    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            i = i // 2
    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)
    def add_all(self, a_list):
        for value in a_list:
            self.insert(value)
    def __iter__(self):
        return PriorityQueueIterator(self)


