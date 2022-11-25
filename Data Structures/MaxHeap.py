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
        else:
            return False
    
    def pop(self):
        
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False

        return max
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        pass

    def __bubbleDown(self, index):
        pass