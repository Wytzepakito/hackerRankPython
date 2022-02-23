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

five.next = one
four.next = five
three.next = four
two.next = three
one.next = two


def has_cycle(head):

    node = head
    hashset = set()

    while(node is not None):
        if node in hashset:
            return 1
        else:
            hashset.add(node)
        node = node.next

    return 0



print(has_cycle(one))
