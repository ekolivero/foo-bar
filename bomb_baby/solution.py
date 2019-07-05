def solution(x, y):
    m,f = int(x), int(y)
    
    # Declare generation cnt --> initial 0
    
    generation = 0 
    
    # Loop till min number between m and f is 1
    
    while min(m,f) != 1:
        # return impossibile if the number are multiple each other
        if max(m,f) % min(m,f) == 0:
            return "impossible"
        
        # increment the generations
        
        generation += max(m,f) / min(m,f)
        
        # declare new values of m, f
        
        (m, f) = (max(m,f) % min(m,f), min(m,f))
        
    return str(generation + max(m,f) - 1)
