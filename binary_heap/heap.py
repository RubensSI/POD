class BinHeap(object):
    def __init__(self):
        # lista que representa as posições da arvore
        self.heapList = [0]  # inicia com a posição zero

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

    def findMin(self):
        return self.heapList[1]

    def delMin(self):
        retval = None
        if len(self.heapList) > 1:
            retval = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDonw(1)
        return retval

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)

            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp

            i = mc


    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[2 * 1] < self.heapList[i * 2 + 1]:
                return 2 * i
            else:
                 return i * 2 + 1 

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return self.currentSize
    
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:] # alist recebe 0 na primeira posição, mais o restante da lista => alist
        while i > 0:
            self.percDown(i)
            i = i - 1
            print(self.heapList)


if __name__ == "__main__":

    heap = BinHeap()
    
    array = [34, 2, 5, 12, 5, 43, 1]

    heap.buildHeap(array)