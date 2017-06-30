

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

head = Node(7)
end = head

def add(node):
    global end
    end.next = node
    node.prev = end
    end = node
    return

def printLinkedList():
    global head
    start = head
    while (True):
        print start.value
        if (start.next == None):
            break
        start = start.next



add(Node(5))
add(Node(3))
add(Node(1))
printLinkedList()
