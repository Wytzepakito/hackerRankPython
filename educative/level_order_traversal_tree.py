

from socket import NI_NUMERICSERV


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def level_order_traversal(root):
    queue = []
    string = ""

    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node.data)

        if (node.left != None):
            queue.append(node.left)

        if (node.right != None):
            queue.append(node.right)








hundred = Node(100)

fifty = Node(50)
twohundred = Node(200)
hundred.left = fifty
hundred.right = twohundred

twentyfive = Node(25)
seventyfive = Node(75)

fifty.left = twentyfive
fifty.right =seventyfive

threehundredfifty = Node(350)
fourhundred = Node(400)
twohundred.left = threehundredfifty
twohundred.right = fourhundred


ten = Node(10)
five = Node(5)
twentyfive.left = ten 
twentyfive.right  = five

seven = Node(7)
eight = Node(8)
seventyfive.left = seven
seventyfive.right = eight

nine = Node(9)
six = Node(6)

threehundredfifty.left = nine
threehundredfifty.right = six

four = Node(4)
three = Node(3)

fourhundred.left = four
fourhundred.right = three





level_order_traversal(hundred)