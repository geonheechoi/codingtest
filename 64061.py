def solution(board, moves):
    '''
    board = 
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
    
    moves = [1,5,3,5,1,2,1,4]

    return == 4
    '''
    
    answer = 0
    basket = []
    
    for move in moves:
        if board[-1][move-1] == 0:
            continue
            
        depth = 0
        while board[depth][move-1] == 0:
            depth += 1
        item = board[depth][move-1]
        
        basket.append(item)
        board[depth][move-1] = 0
        
        while len(basket) >= 2 and basket[-2] == basket[-1]:
            basket.pop()
            basket.pop()
            answer += 2
        
    return answer
