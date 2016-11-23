import sys
import math

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis

lines = []
for i in xrange(height):
    line = raw_input()  # width characters, each either 0 or .
    lines.append(line)

for i in range(0, len(lines), 1):
    for j in range(0, len(lines[i]), 1):
        if lines[i][j] != '.':
            y1, x1 = str(i), str(j)
            try:
                k = j
                while True:
                    if lines[i][k + 1] != '.':
                        y2, x2 = str(i), str(k + 1)
                        break
                    else:
                        y2, x2 = "-1", "-1"
                    k += 1
            except:
                y2, x2 = "-1", "-1"
            try:
                l = i
                while True:
                    if lines[l + 1][j] != '.':
                        y3, x3 = str(l + 1), str(j)
                        break
                    else:
                        y3, x3 = "-1", "-1"
                    l += 1
            except:
                y3, x3 = "-1", "-1"
        else:
            continue

        print x1 + " " + y1 + " " + x2 + " " + y2 + " " + x3 + " " + y3
