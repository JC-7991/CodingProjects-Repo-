class MaxHeap:

    def __init__(self, items = []):

        super().__init__()
        self.heap = 0
        
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)