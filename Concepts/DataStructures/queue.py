class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

head = Node(7)
end = head
# reference to both beginning and the end
# difference lies in how things get added and deleted
# aka enque and dequeue

def enque(node):
    global head
    head.prev = node
    node.next = head
    head = node
    return

def dequeue():
    global end
    print end.value
    end = end.prev
    end.next = None
    return

#with reference to the beginning
def printLinkedList():
    global head
    start = head
    while (True):
        print start.value
        if (start.next == None):
            break
        start = start.next


enque(Node(5))
enque(Node(3))
enque(Node(1))
dequeue()
dequeue()
dequeue()
