from collections import deque
from typing import Any, Optional

class Stack:
    def __init__(self):
        self._data: list[Any] = []
    
    def push(self, item):
        self._data.append(item)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None  # none if empty
        return self._data[-1]
    
    def __len__(self) -> int:
        return len(self._data)
    
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")  # if you try to dequeue from empty
        return self._data.popleft() 
    
    def peek(self):
        if self.is_empty():  
            return None  # none if the queue is empty
        return self._data[0]
    
    def is_empty(self) -> bool:
        return len(self._data) == 0 
    
stack = Stack()
print("\n--- Testing Stack ---")
stack.push(10)
stack.push(20)
print("peek:", stack.peek())  # expected: Peek: 20
item = stack.pop()
print("popped:", item)       # expected: Popped: 20
print("empty?", stack.is_empty())   # expected: empty? False
stack.pop()
print("empty after last pop?", stack.is_empty())   # expected: Is empty after last pop? True

queue = Queue()
print("\n--- Testing Queue ---")
queue.enqueue('1')
queue.enqueue('2')
print("dequeue:", queue.dequeue())     # expected: Dequeue: 1
print("peek:", queue.peek())           # expected: Peek: 2
print("empty?", queue.is_empty())   # expected: empty? False
queue.dequeue()
print("empty after last dequeue?", queue.is_empty())