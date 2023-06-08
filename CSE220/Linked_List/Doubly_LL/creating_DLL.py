class Node:

    def __init__(self, data):
        self.data = data 
        self.nextNode = None 

class LinkedList:

    def __init__(self):
        self.head = None 
        self.numOfNodes = 0 

    def insert_start (self, data):
        self.numOfNodes += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insert_end (self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head
        while actual_node.nextNode != None : 
            actual_node = actual_node.nextNode
        actual_node.nextNode =new_node

    def size_of_LL (self):
        return self.numOfNodes
    
    def traverse(self):
        actual_node = self.head 
        while actual_node != None: 
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove (self, data):
        if self.head is None : 
            return
        actual_node = self.head
        previous_node = None 

        while actual_node != None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        #this is a search miss  
        if actual_node == None: 
            return
        
        self.numOfNodes -= 1 
        
        if previous_node == None: #actual node was a match so need to remove the head
            self.head = actual_node.nextNode
        else: 
            previous_node.nextNode = actual_node.nextNode


    def reverse(self):
        currentNode = self.head 
        prevNode = None
        store_Node = None 

        while currentNode != None:
            store_Node = currentNode.nextNode
            currentNode.nextNode = prevNode
            prevNode = currentNode
            currentNode = store_Node 
        
        self.head = prevNode


linked_list = LinkedList()
linked_list.insert_start(1)
linked_list.insert_start(2)
linked_list.insert_start(3)
linked_list.insert_end(5)
linked_list.insert_end(111)

# linked_list.traverse()
linked_list.remove(1000)
linked_list.traverse()
linked_list.remove(1)
linked_list.traverse()
linked_list.remove(111)
linked_list.traverse()
print('Reversed Linked List: ')
linked_list.reverse()
linked_list.traverse()