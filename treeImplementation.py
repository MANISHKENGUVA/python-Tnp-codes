class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
        print("Node id created")


 
root = Node(1)
second =Node(2)
third=Node(3)
root.next=second
root.prev=third


