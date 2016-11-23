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
# Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.

raw_input()
m=0
for t in map(int,raw_input().split()):
    if(m==0)or(abs(t)<abs(m))or((t==-m)and(t>0)):m=t
print(m)
