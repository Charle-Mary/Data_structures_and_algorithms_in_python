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

    def remove(self, data):
        
        if self.head is None:
            return

        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
        
    def removeSortedDuplicate(self):
        if self.head is None:
            return

        currentNode = self.head
        while currentNode.nextNode is not None:
            if currentNode.data != currentNode.nextNode.data:
                currentNode = currentNode.nextNode
            else:
                self.size -= 1
                currentNode.nextNode = currentNode.nextNode.nextNode

    def removeUnsortedDuplicate(self):
        unique = dict()

        currentNode  = self.head
        previousNode = None
        while currentNode is not None:
            if currentNode.data  in unique:
                self.size -= 1
                previousNode.nextNode = currentNode.nextNode
                currentNode = None
            else:
                unique[currentNode.data] = 1
                previousNode = currentNode
            currentNode = previousNode.nextNode
            

    def size1(self):
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

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode



linkedlist = LinkedList()

linkedlist.InsertStart(12)
linkedlist.InsertStart(13)
linkedlist.InsertStart(12)
linkedlist.InsertStart(13)
linkedlist.InsertStart(162)
linkedlist.InsertStart(192)
linkedlist.InsertStart(192)

print(linkedlist.size1())
print('\n')

linkedlist.traverseList()
print('\n')

linkedlist.removeUnsortedDuplicate()
linkedlist.traverseList()
print('\n')

print(linkedlist.size1())

