def solution(s):
    # Get the position of all emplyee walking to the right
    l_right = [idx for idx, item in enumerate(s.lower()) if '>' in item]
    # Get the position of all emplyee walking to the left
    l_left = [idx for idx, item in enumerate(s.lower()) if '<' in item]
    
    # Number of salutes done.
    salutes = 0
    
    for right in l_right:
        for left in l_left:
            if (left > right):
                # When two employee will cross I increment the salutes.
                salutes = salutes + 2
    
    return salutes
