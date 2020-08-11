class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.length += 1
            self.head = new_node
            self.tail = new_node
        else:
            self.length += 1
            self.tail.set_next(new_node)
            self.tail = new_node
            
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            val = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        
        else:
            current = self.head
            val = self.tail.get_value()            
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(new_next=None)
            self.length -= 1
            return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return val
        