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
link.head = Node(12)#first node(12) is connected to the self.head 
second =Node(14)#creation of the 2 node
third=Node(16)#creation of the 2 node
fouth=Node(17)#creation of the 2 node
fifth=Node(18)#creation of the 2 node
link.head.next=second#connecting node(14) to node(12)
second.next=third #connecting node(16) to node(14)
third.next=fouth #connecting node(17) to node(16)
fouth.next=fifth #connecting node(18) to node(17)

count=0 #count the no of variables


current = link.head #count 
while current != None :
    count+=1
    print(current.data)
    current = current.next
    
print(count)#midd value calculation
mid=(count //2)
print(mid)
print("broooooo")
count = 0 #count value turns to Zero for the memory constraint
temp = link.head

while count < mid :#traversing the linkedlist until the mid 
    prev = temp     #prev was lately updated then the temp
    print(temp.data)
    temp = temp.next
    count += 1
prev.next=(prev.next).next # for deleting the current element we used prev the linked list 
print("after deletion")
current = link.head
while current != None :#for displaying
    count+=1
    print(current.data)
    current = current.next






