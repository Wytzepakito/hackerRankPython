class Node:

    def __init__(self, data):
        self.data = data
        self.others = []
        self.marked = False



def search(root):

    queue = []
    root.marked = True
    queue.append(root)


    while(len(queue)!= 0):
        
        node = queue.pop(0)
        print(node.data)
        if node.data == "E":
            return True
        for other in node.others:
            if other.marked == False:
                other.marked = True
                queue.append(other)

    return False







ee = Node("E")

bb = Node("B")

cc = Node("C")

cc.others.extend([ee, bb])

ff = Node("F")

ff.others.extend([cc])

gg = Node("G")

gg.others.extend([ff])

qq = Node("Q")

qq.others.extend([ff])

jj = Node("J")

tt = Node("T")

tt.others.extend([qq, gg, jj])

rr = Node("R")



pp = Node("P")

ss = Node("S")

pp.others.extend([rr, tt, ss])






print(search(pp))