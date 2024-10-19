def solution(moves):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = 0
    d = 0

    for move in moves:
        if move == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif move == 'R': 
            d = (d + 1) % 4
        else: 
            d = (d - 1) % 4
    return (x, y)
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))