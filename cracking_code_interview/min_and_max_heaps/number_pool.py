"""
Create a number pool 1.. infinity which has 2 methods
checkin(somenumber) and checkout()

checkout gives the minimum number checked in.
checkin returns a checkedout number back into the numberpool for new querying
checkout() gives 1
checkout() gives 2
checkin(1)
checkout() gives 1
checkout() gives 3
"""
import heapq

class NumberPool:

    heap = []
    last_returned = 0

    def checkout(self):
        if len(self.heap)> 0:
            return heapq.heappop(self.heap)
        else:
            temp = self.last_returned
            self.last_returned +=1
            return temp




    def checkin(self, num):
        heapq.heappush(self.heap, num)




numPool = NumberPool()

k = numPool.checkout()
r = numPool.checkout()
print(numPool.checkout())
print(numPool.checkout())
print(numPool.checkout())
numPool.checkin(r)
numPool.checkin(k)
print(numPool.checkout())
print(numPool.checkout())



