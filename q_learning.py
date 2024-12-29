import random

Q = {}

def choose_action(state, epsilon=0.1):
    if state not in Q:
        Q[state] = {action: 0 for action in ['left', 'right', 'up', 'down']}
    if random.random() < epsilon: # exploration
        return random.choice(['left', 'right', 'up', 'down'])
    else: # exploitation
        return max(Q[state], key=Q[state].get)

def update_q_value(state, action, reward, new_state, alpha=0.1, gamma=0.9):
    if new_state not in Q:
        Q[new_state] = {action: 0 for action in ['left', 'right', 'up', 'down']}
    Q[state][action] = Q[state][action] + alpha * (
        reward + gamma * max(Q[new_state].values()) - Q[state][action]
    )