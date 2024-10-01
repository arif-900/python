#stack operations through list
stack=[]
size=5
def display():
        print("Stack items are :")
        for item in stack:
            print(stack)
def push(item):
        print(f"push an item into the stack {item}")
        if len(stack)<size:
            stack.append(item)
        else:
            print("Stack is full")
def pop():
        if len(stack)<size:
            print(f"pop item from stack {stack.pop}")
        else:
            print("Stack is empty")
def main():
        push(10)
        push(20)
        push(30)
        push(40)
       
        pop()
        display()
        push(50)
        display()
        pop()
        pop()
        pop()
        pop()
        pop()
if __name__ == "__main__":
    main()