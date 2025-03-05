import random

def total_earning (N):
    total = 0
    outcomes = ['red'] * 9 + ['black'] * 9 + ['green'] * 1
    
    for _ in range(N):
        result = random.choice(outcomes)
        
        if result == 'black':
            total += 1
        else:
            total -= 1
            
    return total         