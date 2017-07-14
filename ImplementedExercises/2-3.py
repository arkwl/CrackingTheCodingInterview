class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

top = Node("a")
head = Node("a")
end = head

def push(node):
    global top
    top.next = node
    node.prev = top
    top = node
    return

def pop():
    global top
    if (top.prev == None):
        return
    print top.value
    top = top.prev
    top.next = None

def add(node):
    global end
    end.next = node
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


add(Node("b"))
add(Node("c"))
add(Node("d"))
add(Node("e"))

previousSlow = ""
slow = head
fast = head
while (True):
    if (fast.next == None):
        break
    previousSlow = slow
    slow = slow.next
    fast = fast.next.next

print("slow value: " + slow.value)
print("fast value: " + fast.value)

previousSlow.next = slow.next
printLinkedList()
