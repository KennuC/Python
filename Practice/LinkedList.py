class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        


class SLinkedList:
    def __init__(self):
        self.headval = None

    def printList(self):
        currentNode = self.headval
        if (currentNode != None):
            print(currentNode.dataval)
            currentNode = currentNode.nextval
        else:
            print("No Nodes")

    def appendNode(self, Node):
        currentNode = self.headval
        while (currentNode.nextval != None):
            currentNode = currentNode.nextval

        currentNode.nextval = Node
    
    def removeLastNode(self):
        currentNode = self.headval
        if (currentNode.nextval == None):
            self.headval = None
            return -1 
        while (currentNode.nextval.nextval != None):
            currentNode = currentNode.nextval
        currentNode.nextval = None 
            
        
        

list1 = SLinkedList()
list1.headval = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")
node4 = Node("Thu")
list1.appendNode(node2)
list1.appendNode(node3)
list1.appendNode(node4)

list1.removeLastNode()
list1.removeLastNode()
list1.removeLastNode()
list1.removeLastNode()


list1.printList()