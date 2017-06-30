

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

end = Node(7)

def add(node):
    global end
    end.next = node
    node.prev = end
    end = node
    return

def printLinkedList():
    head = end
    while (head.value != None):
        print head.value
        head = head.prev
        if (head.value == None):
            break

add(Node(5))
add(Node(3))
add(Node(1))
printLinkedList()
