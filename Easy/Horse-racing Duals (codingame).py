
strength = []

n = int(raw_input())
for i in xrange(n):
    pi = int(raw_input())
    strength.append(pi)

sorted_strength = sorted(strength)
print min(abs(i - j) for i, j in zip(sorted_strength, sorted_strength[1:]))
