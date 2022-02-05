


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next


    def add_to_list(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:

            last = last.next

        last.next = newNode



def merge_sorted(listA, listB):
    if listA.head is None:
        return listB.head
    if listB.head is None:
        return listA.head

    new_list = LinkedList()

    lastA = listA.head
    lastB = listB.head



    while(lastA.next != None or lastB.next != None):
        
        if lastA.data < lastB.data:
            new_list.add_to_list(lastA.data)
            lastA = lastA.next
        else:
            new_list.add_to_list(lastB.data)
            lastB = lastB.next

    if lastA.data < lastB.data:
        new_list.add_to_list(lastA.data)
        new_list.add_to_list(lastB.data)
    else:
        new_list.add_to_list(lastB.data)
        new_list.add_to_list(lastA.data)

    return new_list.head

    


    




listA = LinkedList()
listB = LinkedList()


listA.add_to_list(5)
listA.add_to_list(10)
listA.add_to_list(15)

listB.add_to_list(2)
listB.add_to_list(3)
listB.add_to_list(20)



final_list =LinkedList()
final_list.head = merge_sorted(listA, listB)

