from array import array


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
    def getParent():
        return(self.parent)
    def getWord():
        return (self.word)


class Node(object):
    def __init__(self, data, nextNode=None):
        self.__data = data
        self.nextNode = nextNode
    #self.__prev = None
    #return self.__data

    def getdata(self):
        return str(self.__data)
    
    def __str__(self):
        return str(self.__data)

#Skapar en queue.
class LinkedQ():
    def __init__(self):
        self.first = None
        self.last = self.first
        self.length = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.nextNode = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.first:
            out = self.first.getdata()
            self.first = self.first.nextNode
            self.length -= 1
            return (out)
            
    def peek(self):
        if not self.isEmpty():
            return self.first.getdata()
        else:
            return None
    def isEmpty(self):
        if self.first is None:
            return True
        else:
            return False
