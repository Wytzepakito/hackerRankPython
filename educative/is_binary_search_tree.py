
import math
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_of_tree(root):
    maxi = -math.inf

    queue = []
    queue.append(root)

    while(len(queue) != 0):
        node = queue.pop(0)

        if node.data > maxi:
            maxi = node.data

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)
    return(maxi)


def min_of_tree(root):
    mini = math.inf

    queue = []
    queue.append(root)

    while(len(queue) != 0):
        
        node = queue.pop(0)


        if node.data < mini:
            mini = node.data

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)

    return(mini)

        



def is_bst(root):
    

    queue = []
    queue.append(root)

    while(len(queue) !=0):
        node = queue.pop(0)


        if node.left != None:
            if max_of_tree(node.left)> node.data:
                return("NO")
        if node.right != None:
            if min_of_tree(node.right)< node.data:
                return("NO")

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)

    return("YES")



def is_bst_rec(root, min_value, max_value):
    if root != None:

        print(f"min val {min_value}, root {root.data}, max val {max_value}")
    if root == None:
        return True

    if root.data < min_value or root.data > max_value:
        return False

    return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
    return is_bst_rec(root, -math.inf, math.inf)








hundred = Node(100)

fifty = Node(50)
twohundred = Node(200)

hundred.left = fifty
hundred.right = twohundred

twentyfive = Node(25)
seventyfive = Node(75)

fifty.left = twentyfive
fifty.right = seventyfive

twelve = Node(12)
forty = Node(40)

twentyfive.left = twelve
twentyfive.right = forty

sixty = Node(60)
ninety = Node(90)

seventyfive.left = sixty
seventyfive.right = ninety

hundredtwentyfive = Node(125)
threehundredfifty = Node(350)

twohundred.left = hundredtwentyfive
twohundred.right = threehundredfifty

hundredten = Node(110)
hundredforty = Node(140)

hundredtwentyfive.left = hundredten
hundredtwentyfive.right = hundredforty

threehundredthirthy = Node(330)
threehundredeighty = Node(380)


threehundredfifty.left = threehundredthirthy
threehundredfifty.right = threehundredeighty




#print(min_of_tree(hundred))
print(is_bst(hundred))


# hundred = Node(100)

# fifty = Node(50)
# twohundred = Node(200)

# hundred.left = fifty
# hundred.right = twohundred

# twentyfive = Node(25)
# seventyfive = Node(75)

# fifty.left = twentyfive
# fifty.right = seventyfive

# ninety = Node(90)
# threehundredfifty = Node(350)

# twohundred.left = ninety
# twohundred.right = threehundredfifty


# print(is_bst(hundred))
