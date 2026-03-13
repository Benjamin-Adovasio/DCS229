######################################
# DCS 229 -- Stack
# Stack data structure implemented with Linked List
# Date:
# Name:
# Resources Used:
##########################################


from LinkedList import *
class EmptyError(Exception):
    ''' class extending Exception to better document stack errors '''
    def __init__(self, message: str):
        self.message = message

class Stack[T]:
    ''' class to implement a stack ADT using our LinkedList class'''


    def __init__(self):
       
        pass
    def __len__(self) -> int:
        ''' allows the len function to be called using an ArrayStack object, e.g.,
               stack = ArrayStack()
               print(len(stack))
        Returns:
            number of elements in the stack, as an integer
        '''
        pass

    def push(self, item: T) -> None: 
        ''' pushes a given item of arbitrary type onto the stack
        Parameters:
            item: an item of arbitrary type
        Returns:
            None
        '''
        pass

    def pop(self) -> T:
        ''' removes the topmost element from the stack and returns that element
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        pass

    def peek(self) -> T:
        ''' returns the topmost element from the stack without modifying the stack
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        pass

    def is_empty(self) -> bool:
        ''' indicates whether the stack is empty
        Returns:
            True if the stack is empty, False otherwise
        '''
        pass

    def __str__(self) -> str:
        ''' returns an str implementation of the Stack '''
   
        return str(self._data)

def main():
    # add your tests here!
    pass

if __name__ == "__main__":
    main()

