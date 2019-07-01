def solution(total_lambs):
    # fibonacci sequence for getting the max hanchman paid respecting the rules.
    min_henchmen = min_hanchmen_paid(total_lambs)
    # double the first payment for getting the min hanchman paid respecting the rules.
    max_hanchmen = max_hanchman_paid(total_lambs)
    diff_paid = min_henchmen - max_hanchmen
    return diff_paid

def min_hanchmen_paid(total_lambs):
    # helper variables
    a = 0
    b = 1
    fibonacci = [a,b]
    while (sum(fibonacci) <= total_lambs):
        a, b = b, a+b
        fibonacci.append(b)
    
    if (sum(fibonacci) > total_lambs):
        # Commander lambda can't pay the next hanchmen
        fibonacci.pop()
        # Clean helper
        fibonacci.pop(0)
    else:
        # Clean helper
        fibonacci.pop(0)
        
    #return the n of paid hanchmen
    return len(fibonacci)
    
def max_hanchman_paid(total_lambs):
    helper = [1, 2]
    while sum(helper) <= total_lambs:
        helper.append(helper[-1]*2)
    if (sum(helper) > total_lambs):
        # Commander lambda can't pay the next hanchmen
        helper.pop()
    return len(helper)
