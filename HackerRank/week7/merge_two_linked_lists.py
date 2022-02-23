class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



def print_llist(head):

    while(head != None):
        print(head.data, end = ", ")
        head = head.next
    print("")


sixteen = Node(16)
ten = Node(10)
seven = Node(7)
two = Node(2)
one = Node(1)

ten.next = sixteen
seven.next = ten
two.next = seven
one.next = two


seventeen = Node(17)
thirteen = Node(13)
eight = Node(8)
six = Node(6)
five = Node(5)
two2 = Node(2)

thirteen.next = seventeen
eight.next = thirteen
six.next = eight
five.next = six
two2.next = five



def merge_sorted_lists(A, B):


    if A.data > B.data:
        new = B
        B = B.next
    else:
        new = A
        A = A.next
    head = new

    while( not (A is None and B is None)):
        if (B is None):
            new.next = A
            A = A.next
        elif (A is None):
            new.next = B
            B = B.next
        elif (A.data > B.data):
            new.next = B
            B = B.next
        elif (B.data >= A.data):
            new.next = A
            A = A.next

        new = new.next
        

    return head
        
    
new = merge_sorted_lists(two2, one)

print_llist(new)


