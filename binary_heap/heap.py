class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
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
            self.percDown(1)

        return retval

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)

            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp

            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return self.currentSize

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1
            print(self.heapList)

import random
if __name__ == "__main__":
    heap = BinHeap()

    low = [500, 501, 502, 503]
    mid = [300, 301, 302, 303]
    high = [100, 101, 102, 103]

    items = low + mid + high

    random.shuffle(items)
    print('Antes {0}'.format(items))

    heap.buildHeap(items)

    while not heap.isEmpty():
        next = heap.delMin()
        print(next)   