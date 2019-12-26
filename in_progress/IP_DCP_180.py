"""
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only 
one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], 
it should become [1, 4, 2, 3].
"""



import random

def main():
    N = random.randrange(start=5, stop=12, step=1)
    stack = []
    for i in range(N):
        stack.append(random.randrange(start=0, stop=10, step=1))
    queue = []
    print(stack)
    iter = N-1
    while iter>0:
        for i in range(iter):
            queue.append(stack.pop())
        for i in range(iter):
            stack.append(queue.pop(0))
        iter = iter - 1
        for i in range(iter):
            queue.append(stack.pop())
        for i in range(iter):
            stack.append(queue.pop(0))
        iter = iter-1
    print(stack)
    return

if __name__ == "__main__":
    main()