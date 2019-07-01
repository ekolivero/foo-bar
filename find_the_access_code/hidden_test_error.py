# l should be a list of positive integer
# I have to find how many lucky triple (x, y, z) where x divide by y and y divide by z
# first I have to clean the string, if the number are all the same

def solution(l):

    # I should first check if the number are all the same

    pairs = []

    test = (lambda a,b,c : c % b == 0 and b % a == 0)

    for x in l:
        for y in l:
            for z in l:
                if (x < y < z):
                    _help = test(x,y,z)
                    if (_help == True):
                        pairs.append((x,y,z))
    
    clean = cleanString(pairs)

    print (len(clean))
    
    

def cleanString(l):
    return list(dict.fromkeys(l))
