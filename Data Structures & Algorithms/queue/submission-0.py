class Node: 
    def __init__(self, data): 
        self.next = None 
        self.prev = None 
        self.val = data

class Deque:
    
    def __init__(self):
        self.head = Node(-1) 
        self.tail = Node(-1)
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.size = 0


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        prev = self.tail.prev 

        prev.next = new_node 
        new_node.next = self.tail
        new_node.prev = prev
        self.tail.prev = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        prev = self.head.next 

        prev.prev = new_node
        new_node.next = prev 
        new_node.prev = self.head
        self.head.next = new_node 
        self.size += 1

    def pop(self) -> int:

        if self.size != 0:
            delete_node = self.tail.prev

            delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev
            self.size -= 1
            return delete_node.val
        else: 
            return -1 

    def popleft(self) -> int:        
        if self.size != 0:
            delete_node = self.head.next

            delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev 
            self.size -= 1
            return delete_node.val
        else: 
            return -1 

