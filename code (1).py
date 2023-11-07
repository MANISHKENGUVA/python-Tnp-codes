class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print("Node id created")

class LinkedList:
    def __init__(self):
        self.head = None
        print("header Created")

link = LinkedList() 
link.head = Node(1)
second =Node(2)
third=Node(3)
link.head.next=second
second.next=third


current = link.head
while current != None:
    print(current.data)
    current = current.next