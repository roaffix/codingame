# Goal:
# In this exercise, you have to analyze records of temperature to find the closest to zero.
# You need to solve this puzzle using as little characters as possible.
# Rules:
# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered
# closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
# Input:
# Line 1: N, the number of temperatures to analyze
# Line 2: The N temperatures expressed as integers ranging from -273 to 5526
# Output:
# Display 0 (zero) if no temperatures are provided. Otherwise, display the
# temperature closest to 0.


n = int(raw_input())
temps = raw_input().split(' ')
try:
    temp_values = map(int, temps)
    hot, cold = [t for t in temp_values if t > 0], [
        t for t in temp_values if t < 0]
    if not cold:
        print min(hot)
    elif not hot:
        print max(cold)
    else:
        print min(hot) > abs(max(cold)) and max(cold) or min(hot)
except ValueError:
    print 0
