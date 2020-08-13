"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # wrap in a new node
        new_node = ListNode(value)
        # check if the DLL is empty
        if self.head is None and self.tail is None:
            # set head & tail to refer to the new node
            self.length += 1
            self.head = new_node
            self.tail = new_node
        # otherwise (DLL isn't empty)
        else:
            self.length += 1
            # grab the previous head
            prev_head = self.head
            # set head to the new node
            self.head = new_node
            # set the new head's next to old head 
            new_node.next = prev_head
            # set old head's prev to the new head 
            prev_head.prev = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.length -= 1
            # grab the removed value
            removed = self.head
            # set head and tail to none for the node
            self.head = None
            self.tail = None
            # return the removed node
            return removed.value
        else:
            # grab the current head in a variable
            removed = self.head
            # change the old head next's prev to None (replace old head with none)
            removed.next.prev = None
            # update the head to the old head's next
            self.head = removed.next
            self.length -= 1
            return removed.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # wrap in a new node
        new_node = ListNode(value)
        # check if the DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to refer to the new node
            self.length += 1
            self.head = new_node
            self.tail = new_node
        else:
            self.length += 1
            # set current tail's next to the new node
            self.tail.next = new_node
            # set the prior tail to the new node's prev
            new_node.prev = self.tail
            # set the new_node as the tail
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.length -= 1
            # grab the removed value
            removed = self.tail
            #set the head and tail to none
            self.head = None
            self.tail = None
            # return the removed node
            return removed.value
        else:
            self.length -= 1
            # grab the removed node in a variable
            removed = self.tail
            # change the tail to the removed's prev
            self.tail = removed.prev
            # update the new tail's next to None
            self.tail.next = None
            # return the removed node
            return removed.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:
            return None
        # check if there is only one value in the list
        elif self.head == self.tail:
            return None
        # check if the head is the passed in value
        elif self.head == node:
            return None
        else:
            # remove node using delete
            DoublyLinkedList.delete(self, node)
            # add node to head using add_to_head functionality
            DoublyLinkedList.add_to_head(self, node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return None
        # check if there is only one value in the list
        elif self.head == self.tail:
            return None
        # check if the input node is already the tail
        elif self.tail == node:
            return None
        else:
            # remove node using delete
            DoublyLinkedList.delete(self, node)
            # add node to the tail using add_to_tail functionality
            DoublyLinkedList.add_to_tail(self, node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
        # check if there is only one value in the list
        elif self.head == self.tail:
            self.length -= 1
            # set head and tail to None (delete only value)
            self.head = None
            self.tail = None
        # check if the node is the head
        elif self.head == node:
            # use remove_from_head functionality
            DoublyLinkedList.remove_from_head(self)
        # check if the node is the tail
        elif self.tail == node:
            DoublyLinkedList.remove_from_tail(self)
        else:
            self.length -= 1
            # node's next now points to its prev
            node.next.prev = node.prev
            # node's prev now points to its next
            node.prev.next = node.next


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        # check if there is only one value in the list
        elif self.head == self.tail:
            # return that value (it's the only one so it's the largest)
            return self.head.value
        else:
            # set the head to the current position
            current_node = self.head
            # set a max value to replace as we find larger numbers
            max_value = current_node.value
            # iterate through until we reach the tail
            while current_node is not None:
                if current_node.value > max_value:
                    # replace the max with the current
                    max_value = current_node.value
                    # set the next node as the new current node
                    current_node = current_node.next
                else:
                    # set the next node as the new current node
                    current_node = current_node.next
            return max_value