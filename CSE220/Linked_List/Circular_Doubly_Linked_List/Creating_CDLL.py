class Node:
    def __init__(self, value = None ) :
        self.value = value
        self.next = None 
        self.prev = None 

class CircularDoublyLinkedList:
    def __init__(self) :
        self.head = None 
        self.tail = None 
    
    def __iter__(self):
        node = self.head 
        while node: 
            yield node
            node = node.next 
            if node == self.tail.next:
                break 

    def createCircularDDLL( self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

initial = CircularDoublyLinkedList()
initial.createCircularDDLL(1)