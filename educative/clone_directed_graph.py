
class Node:
    def __init__(self, d):
        self.data = d
        self.neighbours = []



def clone_rec(root, passed_neighbours):
    if root == None:
        return

    new_node = Node(str(root.data) + "'")

    passed_neighbours[root] = new_node

    for node in root.neighbours:
        node_ = passed_neighbours.get(node)
        if node_ == None:
            new_node.neighbours.append(clone_rec(node, passed_neighbours))
        else:
            new_node.neighbours.append(node_)
    return new_node



def clone(root):
    passed_neighbours = {}
    new_root = clone_rec(root, passed_neighbours)
    return new_root


def print_nodes(root, passed_members):
    print(root.data)
    print([node.data for node in root.neighbours])

    passed_members.append(root)

    for node_ in root.neighbours:
        if not node_ in passed_members:
            print_nodes(node_, passed_members)





zero = Node(0)
four = Node(4)
three = Node(3)
one = Node(1)
two = Node(2)

zero.neighbours.extend([four, three, two])
four.neighbours.extend([zero, three, one])
three.neighbours.extend([two])
one.neighbours.extend([two])
two.neighbours.extend([zero])



new_node = clone(one)

passed_members = []
print_nodes(new_node, passed_members)
