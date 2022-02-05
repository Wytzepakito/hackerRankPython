

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbitrarily_pointer = None



def deep_copy_arbitrary_pointer(head):
    if head is None:
        return None

    current = head
    new_head = None
    new_prev = None
    ht = {}


    while current != None:
        new_node = Node(current.data)

        new_node.arbitrarily_pointer = current.arbitrarily_pointer

        if new_prev != None:
            new_prev.next = new_node
        else:
            new_head = new_node

        ht[current] = new_node

        new_prev = new_node
        current = current.next

    new_current = new_head

    while new_current != None:
        if new_current.arbitrarily_pointer != None:
            node = ht[new_current.arbitrarily_pointer]

            new_current.arbitrarily_pointer = node


        new_current = new_current.next

    return(new_head)




ninenine = Node(99)

eightone = Node(81)
ninenine.next = eightone

one = Node(1)
eightone.next = one

eightsix = Node(86)
one.next = eightsix

seventwo = Node(72)
eightsix.next = seventwo

ninenine.arbitrarily_pointer = seventwo
eightone.arbitrarily_pointer = eightsix
one.arbitrarily_pointer = one
eightsix.arbitrarily_pointer = seventwo
seventwo.arbitrarily_pointer = eightsix



new_head = deep_copy_arbitrary_pointer(ninenine)
print(new_head)

while new_head != None:
    if new_head.next != None:
        print(f"current {new_head.data} next {new_head.next.data} arbitrary {new_head.arbitrarily_pointer.data}")
    else:
        print(
            f"current {new_head.data}  arbitrary {new_head.arbitrarily_pointer.data}")

    new_head = new_head.next