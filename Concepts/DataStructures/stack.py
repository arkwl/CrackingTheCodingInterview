# is a stack a linked list but only with reference to the top?????????

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

top = Node(None)

def push(node):
    global top
    top.next = node
    node.prev = top
    top = node
    return

def pop():
    global top
    if (top.value == None):
        return
    print top.value
    top = top.prev
    top.next = None

def peek():
    global top
    return top

def isEmpty():
    if (top.value == None):
        return True
    else:
        return False

push(Node(6))
push(Node(5))
push(Node(4))
push(Node(3))
pop()
pop()
pop()
pop()
print(peek().value)
print(isEmpty())
