class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def print(self):
        temp = self.head
        while True:
            temp2 = temp
            temp = temp.next
            if temp is None:
                temp2.print(False)
                return
            else:
                temp2.print(True)

    def add(self, value):
        newNode = Node(value, None)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def delete(self, index = None):
        if index is None:
            self.head = self.head.next
        else:
            if index == 0: 
                if self.head is None:
                    print("Exceeded default values.")
                    return
                self.head = self.head.next  
                return 
            temp = self.head
            prev = None
            curr = 0
            while temp is not None:
                if curr == index:
                    prev.next = temp.next
                    return
                curr += 1
                prev = temp 
                temp = temp.next
            print("Exceeded default values.")
 
class Node():
    def __init__(self, data, next = None):
        self.next = next
        self.data = data
    def print(self, x):
        if x:
            print(self.data,"-> ", end="")
        else:
            print(self.data)

l1 = LinkedList()
l1.add("Jennie")
l1.add("Bill")
l1.print()
l1.delete(2)
l1.print()