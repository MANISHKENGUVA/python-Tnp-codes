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
link.head = Node(12)
second =Node(14)
third=Node(16)
fouth=Node(17)
fifth=Node(18)
link.head.next=second
second.next=third
third.next=fouth
fouth.next=fifth

count=0


current = link.head
while current != None :
    count+=1
    print(current.data)
    current = current.next
    
print(count)
mid=(count //2)
print(mid)
print("broooooo")
count = 0
temp = link.head

while count < mid :
    prev = temp
    print(temp.data)
    temp = temp.next
    count += 1
prev.next=(prev.next).next
print("after deletion")
current = link.head
while current != None :
    count+=1
    print(current.data)
    current = current.next






