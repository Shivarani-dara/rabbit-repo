from collections import deque

def is_goal(state):
    return state == ['W', 'W', 'W', '_', 'E', 'E', 'E']

def get_next_states(state):
    next_states = []
    n = len(state)
    for i in range(n):
        if state[i] == '_':
            continue
        # Move right
        if i+1 < n and state[i+1] == '_':
            new_state = state.copy()
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            next_states.append(new_state)
        # Jump right over one rabbit
        if i+2 < n and state[i+2] == '_' and state[i+1] != '_':
            new_state = state.copy()
            new_state[i], new_state[i+2] = new_state[i+2], new_state[i]
            next_states.append(new_state)
        # Move left
        if i-1 >= 0 and state[i-1] == '_':
            new_state = state.copy()
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            next_states.append(new_state)
        # Jump left over one rabbit
        if i-2 >= 0 and state[i-2] == '_' and state[i-1] != '_':
            new_state = state.copy()
            new_state[i], new_state[i-2] = new_state[i-2], new_state[i]
            next_states.append(new_state)
    return next_states

def bfs(initial_state):
    queue = deque()
    visited = set()
    parent = {}  # To store the path

    state_str = ''.join(initial_state)
    queue.append(initial_state)
    visited.add(state_str)
    parent[state_str] = None

    while queue:
        current = queue.popleft()
        if is_goal(current):
            # Goal reached; reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[''.join(current)]
            return path[::-1]
        for next_state in get_next_states(current):
            next_str = ''.join(next_state)
            if next_str not in visited:
                queue.append(next_state)
                visited.add(next_str)
                parent[next_str] = current
    return None

if __name__ == "__main__":
    initial = ['E', 'E', 'E', '_', 'W', 'W', 'W']
    solution_path = bfs(initial)
    if solution_path:
        print("Solution found in {} steps:".format(len(solution_path)-1))
        for step in solution_path:
            print(' '.join(step))
    else:
        print("No solution found.")
