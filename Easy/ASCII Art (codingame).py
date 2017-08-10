l = int(raw_input())
h = int(raw_input())
t = raw_input()

output = []
input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for i in xrange(h):
    row = raw_input()
    char_width = len(row) / len(input)
    for i in t:
        i = i.upper()
        if i in input:
            char_idx = input.index(i)
        else:
            char_idx = len(input) - 1

        char_start = char_idx * char_width
        char_end = (char_idx + 1) * char_width
        output.append(row[char_start:char_end])
    output.append("\n")

print "".join(output)
