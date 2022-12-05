import math

stack1 = ['G', 'D', 'V', 'Z', 'J', 'S', 'B']
stack2 = ['Z', 'S', 'M', 'G', 'V', 'P']
stack3 = ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F']
stack4 = ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q']
stack5 = ['C', 'L', 'S', 'N', 'F', 'M', 'D']
stack6 = ['R', 'G', 'C', 'D']
stack7 = ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q']
stack8 = ['P', 'F', 'V']
stack9 = ['D', 'R', 'S', 'T', 'J']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

def solution():
    with open("day5/steps.txt", "r") as f:
        steps = f.read().splitlines()
        for step in steps:
            details = step.split(" ")
            quantity = int(details[1])
            source = int(details[3])
            dest = int(details[5])
            # old crane
            # for count in range(quantity):
            #     stacks[dest-1].append(stacks[source-1].pop())

            # new crane
            moving = stacks[source-1][-quantity:]
            for count in range(0, quantity):
                stacks[dest-1].append(moving[count])
                stacks[source-1].pop()

solution()
for stack in stacks:
    print(stack[-1], end="")

