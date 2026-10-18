class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        
        self.stack1.append(x) 
               
    def pop(self) -> int:

        #move stack 1 items to stack 2, pop from stack 2, move back to stack 1
        self.stack2 = []

        while self.stack1:

            curr = self.stack1.pop()
            self.stack2.append(curr) 
        
        popped = self.stack2.pop()

        while self.stack2:

            curr = self.stack2.pop()
            self.stack1.append(curr)
        
        return popped

    def peek(self) -> int:

        self.stack2 = []

        while self.stack1:

            curr = self.stack1.pop()
            self.stack2.append(curr) 

        peeked = self.stack2[-1]

        while self.stack2:

            curr = self.stack2.pop()
            self.stack1.append(curr)
    
        return peeked


        
    def empty(self) -> bool:
       
        return len(self.stack1) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
