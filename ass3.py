import heapq

goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

start = (
    8, 1, 3,
    7, 0, 4,
    6, 2, 5
)


def heuristic(state):
    h = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            h += abs(i // 3 - goal_pos // 3)
            h += abs(i % 3 - goal_pos % 3)

    return h


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_zero = r * 3 + c

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state)

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state, path + [state])
                )

    return None


solution = a_star(start)

if solution:
    print("Solution found!")
    print("Total moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step:", step)
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found!")