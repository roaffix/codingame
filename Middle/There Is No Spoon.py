# Goal:
# The game is played on a rectangular grid with a given size. Some cells contain power nodes. The rest of the cells are empty.
# The goal is to find, when they exist, the horizontal and vertical neighbors of each node.
# Rules:
# To do this, you must find each (x1,y1) coordinates containing a node, and display the (x2,y2)
# coordinates of the next node to the right, and the (x3,y3) coordinates of the next node to the bottom within the grid.
# If a neighbor does not exist, you must output the coordinates -1 -1 instead of (x2,y2) and/or (x3,y3).
# You lose if:
# -You give an incorrect neighbor for a node.
# -You give the neighbors for an empty cell.
# -You compute the same node twice.
# -You forget to compute the neighbors of a node.
# Input:
# Initialization input
# Line 1: one integer width for the number of cells along the x axis.
# Line 2: one integer height for the number of cells along the y axis.
# Next height lines: A string  line  containing  width  characters. A dot
# . represents an empty cell. A zero 0 represents a cell containing a
# node.

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

        print "{} {} {} {} {} {}".format(x1, y1, x2, y2, x3, y3)
