def solution(l):
    cnt = 0
    memo = [0] * len(l)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            print ("value are %d %d " %(i, j))
            if l[j] % l[i] == 0:
                print ("Number ad dividable")
                memo[j] += 1
                print memo[j]
                print memo[i]
                cnt += memo[i]

    return cnt

# This is the working code, the other was failing on some hidden test.
