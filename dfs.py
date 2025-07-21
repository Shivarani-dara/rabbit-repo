def isgoal(state):
    return state == ['W', 'W', 'W', '_', 'E', 'E', 'E']

def nextstates(state):
    states = []
    n = len(state)
    for i in range(n):
        if state[i] == '_':
            continue
        # move right
        if i+1<n and state[i+1]=='_':
            s = state.copy()
            s[i], s[i+1] = s[i+1], s[i]
            states.append(s)
        # jump right
        if i+2<n and state[i+2]=='_' and state[i+1]!='_':
            s = state.copy()
            s[i], s[i+2] = s[i+2], s[i]
            states.append(s)
        # move left
        if i-1>=0 and state[i-1]=='_':
            s = state.copy()
            s[i], s[i-1] = s[i-1], s[i]
            states.append(s)
        # jump left
        if i-2>=0 and state[i-2]=='_' and state[i-1]!='_':
            s = state.copy()
            s[i], s[i-2] = s[i-2], s[i]
            states.append(s)
    return states

def dfs(initial):
    stack = []
    visited = set()
    stack.append((initial, [initial]))

    while stack:
        current, path = stack.pop()
        s = ''.join(current)
        if s in visited:
            continue
        visited.add(s)
        if isgoal(current):
            return path
        for nxt in nextstates(current):
            stack.append((nxt, path + [nxt]))
    return None

init = ['E','E','E','_','W','W','W']
res = dfs(init)
if res:
    print("DFS Solution found:")
    for step in res:
        print(' '.join(step))
else:
    print("No solution")
