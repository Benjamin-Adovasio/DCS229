######################################
# DCS 229 -- Stack
# Stack data structure implemented with Linked List
# Date:
# Name:
# Resources Used: LinkedList.py from Project 4
##########################################


from LinkedList import *
class EmptyError(Exception):
    ''' class extending Exception to better document stack errors '''
    def __init__(self, message: str):
        self.message = message

class Stack[T]:
    ''' class to implement a stack ADT using our LinkedList class'''


    def __init__(self):
       
        ''' initializes an empty stack '''
        self._data = LinkedList()

    def __len__(self) -> int:
        ''' allows the len function to be called using an ArrayStack object, e.g.,
               stack = ArrayStack()
               print(len(stack))
        Returns:
            number of elements in the stack, as an integer
        '''
        return len(self._data)

    def push(self, item: T) -> None: 
        ''' pushes a given item of arbitrary type onto the stack
        Parameters:
            item: an item of arbitrary type
        Returns:
            None
        '''
        self._data.insert_head(item)

    def pop(self) -> T:
        ''' removes the topmost element from the stack and returns that element
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data.remove_head()

    def peek(self) -> T:
        ''' returns the topmost element from the stack without modifying the stack
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data.get_head()

    def is_empty(self) -> bool:
        ''' indicates whether the stack is empty
        Returns:
            True if the stack is empty, False otherwise
        '''
        return len(self._data) == 0

    def __str__(self) -> str:
        ''' returns an str implementation of the Stack '''
   
        return str(self._data)

def main():
    '''test functions'''
    s = Stack() # I added this so stack doesnt need to be reinitialized for each test

    assert len(s) == 0
    assert s.is_empty() is True

    s.push(10)
    assert len(s) == 1
    assert s.peek() == 10

    s.push(20)
    s.push(30)
    assert len(s) == 3
    assert s.peek() == 30

    assert s.pop() == 30
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty() is True

    try:
        s.pop()
        assert False
    except EmptyError:
        pass

    try:
        s.peek()
        assert False
    except EmptyError:
        pass

    print("All Stack tests passed.") #only runs if all previous tests pass

if __name__ == "__main__":
    main()

