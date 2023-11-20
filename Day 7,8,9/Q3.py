def calculate_manhattan_distance(moves):
    # Starting position
    x, y = 0, 0
    for move in moves:
        if move == 'START':
            continue
        elif move == 'STOP':
            break
        elif move == 'UP':
            y += 1
        elif move == 'DOWN':
            y -= 1
        elif move == 'LEFT':
            x -= 1
        elif move == 'RIGHT':
            x += 1
        distance = abs(x) + abs(y)
    
    return distance
moves = ['START', 'UP', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'STOP']
manhattan_distance = calculate_manhattan_distance(moves)
print("Manhattan Distance:", manhattan_distance)