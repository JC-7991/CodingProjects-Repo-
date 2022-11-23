class MaxHeap:

    def __init__(self, items = []):

        super().__init__()
        self.heap = 0

        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        
        if self.heap[1]:
            return self.heap[1]