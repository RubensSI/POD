class BinHeap(object):
    def __init__(self):
        # lista que representa as posições da arvore
        self.heapList = [0] #inicia com a posição zero
        
        # indica o tamanho atual da lista
        self.currentSize = 0
        
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1 
        self.percUp(self.currentSize)
        
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

if __name__ == "__main__":

    heap = BinHeap()
    
    heap.insert(14)
    print(heap.heapList)
    
    heap.insert(33)
    print(heap.heapList)
    
    heap.insert(5)
    print(heap.heapList)
    
    heap.insert(27)
    print(heap.heapList)

    heap.insert(18)
    print(heap.heapList)


