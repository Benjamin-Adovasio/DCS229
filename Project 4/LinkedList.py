######################################
# DCS 229 -- Linked List
# Linked List implementation
# Date: 03/13/2026
# Name: Benjamin Adovasio
# Resources Used: https://docs.python.org/3/tutorial/datastructures.html
##########################################
from __future__ import annotations

# https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
# Want to define our own custom Exception class...

class EmptyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class Node[T]:
    ''' class to implement a single node object in a singly-linked
        linked list '''
    def __init__(self, data: T):
        self.data = data
        self.next = None  # points to another Node object

    def get_data(self) -> T:
        return self.data
    
    def set_data(self, value: T) -> None:
        self.data = value

    def get_next(self) -> Node[T]:
        return self.next
    
    def set_next(self, next_node: Node[T]) -> None:
        self.next = next_node

class LinkedList[T]:
    ''' class to implement a singly-linked linked list '''

    def __init__(self) -> None:
        self.head = None   # the head pointer in the linked list
        self.size = 0

    def __len__(self) -> int:
        ''' returns the number of nodes in the linked list
        
        Returns:
            int - representing the number of nodes in the list
        '''
        return self.size


    def insert_head(self, value: T) -> None:
        ''' adds the given T-type data value to the front of the linked list
        Parameters:
            value: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''

        ## YOUR CODE HERE ##
       
        new_node = Node(value) # create a new node new_node
        new_node.set_next(self.head) # set the new node's next pointer to the current head of the list
        self.head = new_node # update the head pointer to point to the new node
        self.size += 1 # increase the size of the list by 1

    def insert_tail(self, value: T) -> None:
        ''' adds the given T-type data value to the end of the linked list
        Parameters:
            value: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''

        ## YOUR CODE HERE ##
        """
        The insert_tail method creates a new node with the given value and adds it to the end of the linked list. If the list is empty, it sets the head pointer to the new node. Otherwise, it traverses the list until it reaches the last node and updates its next pointer to point to the new node. Finally, it increments the size of the list by 1.
        """
        new_node = Node(value) # create a new node new_node

        if self.head is None:
            self.head = new_node #if the list is empty, set the head pointer to the new node
        else: #else go through list until we reach end and set the last node's next pointer to the new node
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

        self.size += 1 #increase the size of the list by 1

    def remove_head(self) -> T:
        ''' removes the first Node in the linked list, returning the data item
            inside that Node...  Remember to handle the special case of an 
            empty list (what should the head pointers be in that case?)
            and remember to update the head pointer when appropriate.
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''

        # raise an error if list is empty
        # https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
        if self.size == 0:
            raise EmptyError("Cannot remove from an empy list")


        ## YOUR CODE HERE ##

        removed_node = self.head # store the current head node in a variable removed_node
        self.head = self.head.get_next() # update the head pointer to point to the next node in the list (which could be None if there was only one node)

        self.size -= 1 #decrease the size of the list by 1
        return removed_node.get_data() # return the data item from the removed node       

    def remove_tail(self) -> T:
        ''' removes the last Node in the linked list, returning the data item
            inside that Node...  Remember to handle the special case of an 
            empty list

        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        # raise an error if list is empty
        if self.size == 0:
            raise EmptyError("Cannot remove from an empy list")
    
        ## YOUR CODE HERE ##

        """
        If the list has only one node, we can simply remove the head and return its data. Otherwise, we need to traverse the list to find the second-to-last node, update its next pointer to None, and return the data from the last node.
        """
        if self.head.get_next() is None: #continue if the list has only one node
            removed_data = self.head.get_data() #return the data
            self.head = None #set the head to none
            self.size -= 1 #decrease the size of the list by 1
            return removed_data #return the data from the removed node

        current = self.head

        while current.get_next().get_next() is not None: #while the next node's next pointer is not None, keep going
            current = current.get_next() #move current to the next node

        removed_data = current.get_next().get_data()
        current.set_next(None)

        self.size -= 1 #decrease the size of the list by 1
        return removed_data #return the data from the removed node


    def __str__(self):
        ''' returns a str representation of the linked list data
        Returns:
            an str representation of the linked list, showing head pointer
                and data tiems
        '''
        str_ = "head->"

        # start out at the head Node, and walk through Node by Node until we
        # reach the end of the linked list (i.e., the ._next entry is None)
        ptr_ = self.head
        while ptr_ is not None:
            str_ += "[" + str(ptr_.get_data()) + "]->" 
            ptr_ = ptr_.get_next()  # move ptr_ to the next Node in the linked list

        if self.head != None:
            str_ = str_[:-2]  # remove trailing "->"
        str_ += "<-tail"
        return str_

def main():
    # create a LinkedList and try out some various adds and removes
    ll = LinkedList()
    try:
        ll.remove_head()
    except EmptyError as err:
        print(err)

    ll.insert_head(8)
    assert len(ll) == 1
    removed = ll.remove_head()
    assert removed == 8
    assert len(ll) == 0

    ll.insert_tail(6)
    ll.insert_tail(7)
    ll.insert_tail(5)
    print(ll)
    assert len(ll) == 3

    removed = ll.remove_tail()
    assert removed == 5
    assert len(ll) == 2

    # ADD MORE TESTS

    # test inserting multiple at head
    ll.insert_head(1)
    ll.insert_head(2)
    ll.insert_head(3)
    assert len(ll) == 5
    print(ll)

    # test removing head repeatedly
    assert ll.remove_head() == 3
    assert ll.remove_head() == 2
    assert len(ll) == 3

    # test removing tail until empty
    assert ll.remove_tail() == 7
    assert ll.remove_tail() == 6
    assert ll.remove_tail() == 1
    assert len(ll) == 0

    # test removing from empty again
    try:
        ll.remove_tail()
    except EmptyError:
        print("Correctly caught empty list error")
        
if __name__ == "__main__":
    main()