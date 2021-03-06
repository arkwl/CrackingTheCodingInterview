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
    top = top.prev
    top.next = None

def add(node):
    global end
    end.next = node
    end = node
    return

add(Node("b"))
add(Node("c"))
add(Node("d"))
add(Node("e"))

k = 2


start = head
while (True):
    print start.value
    push(start)
    if (start.next == None):
        break
    start = start.next

for i in range(k):
    pop()
print("kth value: "+top.value)
