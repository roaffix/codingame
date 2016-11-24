# Goal:
# Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual,
# only two horses will participate in the race. In order for the race to be interesting,
# it is necessary to try to select two horses with similar strength.
# Write a program which, using a given number of strengths, identifies the two closest
# strengths and shows their difference with an integer (≥ 0).
# Input:
# Line 1: Number N of horses
# The N following lines: the strength Pi of each horse. Pi is an integer.
# Output:
# The difference D between the two closest strengths. D is an integer
# greater than or equal to 0.

strength = []

n = int(raw_input())
for i in xrange(n):
    pi = int(raw_input())
    strength.append(pi)

sorted_strength = sorted(strength)
print min(abs(i - j) for i, j in zip(sorted_strength, sorted_strength[1:]))
