class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#stack
top = Node("a")
#list
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
    value = top
    top = top.prev
    top.next = None
    return value

def add(node, llist):
    llist.next = node
    llist = node.next
    return

def printLinkedList(node):
    start = node
    while (True):
        print start.value
        if (start.next == None):
            break
        start = start.next


add(Node("b"), end)
printLinkedList(head)
print(" ")
add(Node("c"), end)
printLinkedList(head)
print(" ")
add(Node("b"), end)
printLinkedList(head)
print(" ")
add(Node("a"), end)
printLinkedList(head)
print(" ")

start = head
length = 0
while (True):
    print start.value
    length += 1
    push(start)
    if (start.next == None):
        break
    start = start.next

reverse = Node("")
for i in range(length):
    add(pop(), reverse)

printLinkedList(head)
printLinkedList(reverse)
