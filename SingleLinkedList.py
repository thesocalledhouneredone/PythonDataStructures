class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, someData):
        newNode = Node(someData)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
        print("End of List")

    def lengthOfList(self):
        len = 0
        currentNode = self.head
        while currentNode:
            len += 1
            currentNode = currentNode.next
        print("Length of List: ", len-1)