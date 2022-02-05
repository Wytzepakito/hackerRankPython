import math

class Stack:
    l1 = []

    mini = math.inf


    def push(self, num):
        l1.append(num)
        if num < mini:
            mini = num
        

    def min(self):
        return mini


    def pop(self):
        ret = l1.pop()
        if l1 == mini:
            mini = min(l1)
        
        return ret