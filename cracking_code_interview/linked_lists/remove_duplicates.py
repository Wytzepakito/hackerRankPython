from os import remove


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):

    node = head

    while(node != None):
        print(node.data)

        node = node.next

def is_node_in_list(data, head):

    node = head

    while(node != None):
        if node.data == data:
            return True

        node = node.next

    return False



def remove_dups(head):

    

    if is_node_in_list(head.data, head.next):
        head = head.next


    node = head

    while(node.next != None):
        if node.next.next != None:
            result = is_node_in_list(node.next.data, node.next.next)
            if result == True:
                node.next = node.next.next
        

        node = node.next
    return head





def remove_dups_buf(head):

    node = head

    hashset = set()
    hashset.add(node.data)
    
    while (node.next != None):
        if not node.next.data in hashset:
            hashset.add(node.next.data)
        else:
            if node.next.next != None:
                node.next = node.next.next
            else:
                node.next = None
                break

            

        node = node.next
    return head
        








one = Node(1)

six = Node(6)
one.next = six

one2 = Node(1)
six.next = one2

seven = Node(7)
one2.next = seven

three = Node(3)
seven.next = three

three2 = Node(3)
three.next = three2


print_list(one)

head =remove_dups(one)
print("================")

print_list(head)