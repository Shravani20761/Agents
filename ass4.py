from collections import deque

# Generate all possible next states
def get_successors(state):
    successors = []
    stacks = [list(stack) for stack in state]

    for i in range(len(stacks)):
        if not stacks[i]:
            continue

        block = stacks[i][-1]

        # Move it to every other stack
        for j in range(len(stacks)):
            if i == j:
                continue

            new_stacks = [s[:] for s in stacks]
            new_stacks[i].pop()
            new_stacks[j].append(block)

            # Remove empty stacks
            new_stacks = [tuple(s) for s in new_stacks if s]
            successors.append(tuple(new_stacks))

        # Move block to a new stack (table)
        new_stacks = [s[:] for s in stacks]
        new_stacks[i].pop()
        new_stacks.append([block])

        new_stacks = [tuple(s) for s in new_stacks if s]
        successors.append(tuple(new_stacks))

    return successors


# Breadth First Search
def bfs(start, goal):
    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        for nxt in get_successors(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [current]))

    return None


# Display state
def print_state(state):
    print("-" * 25)

    for i, stack in enumerate(state):
        print(f"Stack {i+1}: {list(stack)}")

    print("-" * 25)


# Initial state
initial = input("Enter initial stack (bottom to top): ").upper()

start = (tuple(initial),)

# Goal state
goal = (('A', 'B', 'C'),)

# Find solution
solution = bfs(start, goal)

if solution:
    print("Solution Found!")

    for step, state in enumerate(solution):
        print(f"Step {step}")
        print_state(state)

else:
    print("No solution found.")