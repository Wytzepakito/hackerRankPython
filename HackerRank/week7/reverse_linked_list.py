class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



def print_llist(head):

    while(head != None):
        print(head.data, end = ", ")
        head = head.next
    print("")



def reverse_linked_list(head):

    node = head
    new_node = None

    while(node.next != None):
        if new_node == None:
            new_node = Node(node.data)
        next_new_node = Node(node.next.data)
        next_new_node.next = new_node

        new_node = next_new_node

        node = node.next

    return new_node





five = Node(5)
four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)

four.next = five
three.next = four
two.next = three
one.next = two 


print_llist(one)

reversed = reverse_linked_list(one)

print_llist(reversed)