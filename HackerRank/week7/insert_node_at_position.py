class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_llist(head):

    while(head != None):
        print(head.data, end=", ")
        head = head.next
    print("")




five = Node(5)
four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)

four.next = five
three.next = four
two.next = three
one.next = two


def insert_node_at_position(llist, data, position):

    node = llist
    current_position = 1
    while(current_position != position):

        node = node.next
        current_position +=1

    new_node = Node(data)
    temp = node.next
    node.next = new_node
    new_node.next = temp
    return llist





head = insert_node_at_position(one, 33, 2)

print_llist(head)