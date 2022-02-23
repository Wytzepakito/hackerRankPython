import os
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node



class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


six = Node(6)
four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)

six.prev = four
four.next = six
four.prev = three
three.next = four
three.prev = two
two.next = three



def print_llist(head):

    while(head != None):
        print(head.data, end=", ")
        head = head.next
    print("")



def sortedInsert(llist, data):

    node = llist

    while(node.next is not None and node.data < data):


        node = node.next
    # insert at start
    if node.prev is None:
        new_node = Node(data)
        node.prev = new_node
        new_node.next = node
        return new_node
    elif node.data < data:
        pass
    else:
        node = node.prev

    ### insert somewhere in the middle
    if not node.next is None:

        temp = node.next
        new_node = Node(data)
        # Insert new node after 
        node.next = new_node
        new_node.prev = node
        new_node.next = temp
        temp.prev = new_node
        
    else:
        # insert at the end

        new_node = Node(data)
        node.next = new_node
        new_node.prev = node

    return llist



print_llist(two)


inserted = sortedInsert(two, 1)


print_llist(inserted)


inserted = sortedInsert(inserted, 5)

print_llist(inserted)


inserted = sortedInsert(inserted, 7)

print_llist(inserted)


llist = DoublyLinkedList()

for num in "23 57 59 59 64 77".split(" "):
    llist.insert_node(int(num))

llist2 = sortedInsert(llist.head, 53)

print_llist(llist2)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         llist_count = int(input())

#         llist = DoublyLinkedList()

#         for _ in range(llist_count):
#             llist_item = int(input())
#             llist.insert_node(llist_item)

#         data = int(input())

#         llist1 = sortedInsert(llist.head, data)

#         print_doubly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
