from collections import deque

def bfs(x, y, t1, t2, matrix) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((2 * x, 2 * y))
    
    while queue :
        a, b = queue.popleft()
        
        if a == t1 * 2 and b == t2 * 2 :
            return matrix[a][b] // 2
        
        else : 
            for i in range(4) :
                newx = a + row[i]
                newy = b + col[i]
                if 0 <= newx < 102 and 0 <= newy < 102 and matrix[newx][newy] == 1 :
                    queue.append((newx, newy))
                    matrix[newx][newy] = matrix[a][b] + 1

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    matrix = [[-1] * 102 for i in range(102)]
    
    for i in rectangle : 
        x1, y1, x2, y2 = map(lambda x : x * 2, i)
        for i in range(x1, x2 + 1) :
            for j in range(y1, y2 + 1) :
                if x1 < i < x2 and y1 < j < y2 :
                    matrix[i][j] = 0
                    
                elif matrix[i][j] != 0 :
                    matrix[i][j] = 1
                    
    result = bfs(characterX, characterY, itemX, itemY, matrix)
    
    return result