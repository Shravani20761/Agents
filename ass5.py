from collections import deque

def get_successors(state):
    successors = []
    stacks = [list(s) for s in state]

    for i in range(len(stacks)):
        if not stacks[i]:
            continue

        block = stacks[i][-1]

        # Move block to another existing stack
        for j in range(len(stacks)):
            if i != j:
                new_stacks = [s[:] for s in stacks]
                new_stacks[i].pop()
                new_stacks[j].append(block)

                new_stacks = [tuple(s) for s in new_stacks if s]
                successors.append(tuple(new_stacks))

        # Move block to a new stack
        new_stacks = [s[:] for s in stacks]
        new_stacks[i].pop()
        new_stacks.append([block])

        new_stacks = [tuple(s) for s in new_stacks if s]
        successors.append(tuple(new_stacks))

    return successors


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        for next_state in get_successors(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current]))

    return None


def print_state(state):
    print("-" * 25)

    for i, stack in enumerate(state):
        print("Stack", i + 1, ":", list(stack))

    print("-" * 25)


initial = input("Enter initial stack (bottom to top): ").upper()

start = (tuple(initial),)
goal = (('A', 'B', 'C'),)

solution = bfs(start, goal)

if solution:
    print("\nSolution Found!\n")

    for step, state in enumerate(solution):
        print("Step", step)
        print_state(state)

else:
    print("No solution found.")
