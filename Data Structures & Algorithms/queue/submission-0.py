class Node:
    def __init__(self,val,prev = None , next = None ):
        self.val = val 
        self.prev = None
        self.next = None
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    def appendleft(self, value: int) -> None:
        new_node= Node(value)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            value = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size -= 1
            return value.val
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            value = self.head.next
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            self.size -= 1
            return value.val




