######################################
# DCS 229 -- Linked List
# Linked List implementation
# Date: 03/13/2026
# Name: Benjamin Adovasio
# Resources Used:
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
       
            new_node = Node(value)
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1

    def insert_tail(self, value: T) -> None:
        ''' adds the given T-type data value to the end of the linked list
        Parameters:
            value: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''

        ## YOUR CODE HERE ##

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

        self.size += 1

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

        pass

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

        pass

 


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
    
if __name__ == "__main__":
    main()