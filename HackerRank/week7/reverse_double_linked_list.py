class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



def print_llist(head):

    while(head != None):
        print(head.data, end = ", ")
        head = head.next
    print("")


def reverse(llist):

    node = llist

    while(node.next != None):
        next_node = node.next

        temp = node.prev
        node.prev = node.next
        node.next = temp

        node = next_node
    temp = node.prev
    node.next = node.prev
    node.prev = temp

    return node



five = Node(5)
four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)

five.prev = four
four.next = five
four.prev = three
three.next = four
three.prev = two
two.next = three
two.prev = one
one.next = two 

print_llist(one)
reversed = reverse(one)
print_llist(reversed)