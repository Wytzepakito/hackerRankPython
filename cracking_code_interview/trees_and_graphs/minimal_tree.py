from copyreg import add_extension


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Linked_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_tree(node):

    if node != None:
        if node.left != None and node.right != None:
            print(f"{node.data} has {node.left.data} and {node.right.data}")
        elif node.left == None and node.right != None:
            print(f"{node.data} has None and {node.right.data}")
        elif node.left != None and node.right == None:
            print(f"{node.data} has None and {node.right.data}")
        elif node.left == None and node.right == None:
            print(f"{node.data} has None and None")



        print_tree(node.left)
        print_tree(node.right)






def create_minimal_tree(list1):

    nodes = []

    for num in list1:
        new = Node(num)
        nodes.append(new)

    current_elem = 0
    added_elems = 1

    while(added_elems != len(list1) -1 and added_elems != len(list1)):

        nodes[current_elem].left = nodes[added_elems]
        nodes[current_elem].right = nodes[added_elems + 1]
        current_elem += 1
        added_elems += 2

    return(nodes[0])



def list_of_depth(root):

    queue = []
    queue.append(root)
    nodes_at_level = 1
    count_nodes = 0
    levels = []
    level = []

    has_root = False



    while(len(queue) != 0):

        node = queue.pop(0)


        count_nodes += 1
        if has_root == False:
            root = Linked_Node(node.data)
            linked_node = root
            has_root = True
        else:
            new_linked_node = Linked_Node(node.data)
            linked_node.next = new_linked_node
            linked_node = new_linked_node

        ## Level of nodes complete!
        if count_nodes == nodes_at_level:
            levels.append(root)
            has_root  = False
            count_nodes = 0
            nodes_at_level = nodes_at_level * 2
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)


    levels.append(root)


    for row in levels:
        count = 0
        while(row != None):
            count += 1
            row = row.next
        print(count)














listy = [i for i in range(1, 21)]
print(len(listy))

root = create_minimal_tree(listy)

print_tree(root)



list_of_depth(root)
