# Program 3.2: Stack Simulator Using List
# Implement a Stack using list with functions:
# push(item), pop(), peek(), is_empty(), display().
# Simulate: push 5 items, peek, pop 2 items, display stack.

stack = []

def push(item):
    stack.append(item)
    print(f"Pushed: {item}")

def pop():
    if is_empty():
        print("Stack Underflow! Stack is empty.")
        return None
    removed = stack.pop()
    print(f"Popped: {removed}")
    return removed

def peek():
    if is_empty():
        print("Stack is empty! Nothing to peek.")
        return None
    return stack[-1]

def is_empty():
    return len(stack) == 0

def display():
    print("\n--- Current Stack (Top to Bottom) ---")
    if is_empty():
        print("Stack is Empty.")
    else:
        for item in reversed(stack):
            print(f"| {item} |")
        print("-------")

# Simulation as required by lab task:
print("--- STACK SIMULATION ---")
# 1. Push 5 items
push("Book A")
push("Book B")
push("Book C")
push("Book D")
push("Book E")

# 2. Peek
print("\nTop item (peek):", peek())

# 3. Pop 2 items
pop()
pop()

# 4. Display
display()
