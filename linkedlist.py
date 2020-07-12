class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def InsertStart(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def size(self):
        return self.size

    def size2(self):
        actualNode = self.head
        self.size = 0

        while actualNode.nextNode is not None:
            self.size += 1
            actualNode = actualNode.nextNode

        return size

    def InsertEnd(self, data):
        self.size += 1
        actualNode = self.head
        newNode = Node(data)

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode  = newNode