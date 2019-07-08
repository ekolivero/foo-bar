import itertools

def solution(num_buns, num_required):

    # I'll deal with this problem using combinations
    r = []

    #Applying pegion rule
    comb = list(itertools.combinations(range(num_buns),num_required))
    total = len(comb)*num_required
    # Should be bunnies_per_key = N - M + 1
    bunnies_per_key = num_buns - num_required + 1
    comb1 = list(itertools.combinations(range(num_buns),bunnies_per_key))
    for i in range(num_buns):
        r.append([])

    for i in range(total/bunnies_per_key):
        for j in comb1[i]:
            r[j].append(i)

    return r

print(solution(2, 1))

