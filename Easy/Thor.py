# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
x, y, tx, ty = [int(i) for i in raw_input().split()]

while True:
    # The remaining amount of turns Thor can move. Do not remove this line.
    remaining_turns = int(raw_input())
    if ty == y:
        if tx < x:
            print "E"
            tx += 1
        else:
            print "W"
            tx -= 1
    elif ty > y:
        if tx == x:
            print "N"
            ty -= 1
        elif tx > x:
            print "NW"
            tx -= 1
            ty -= 1
        else:
            print "NE"
            tx += 1
            ty -= 1
    elif ty < y:
        if tx == x:
            print "S"
            ty += 1
        elif tx > x:
            print "SW"
            tx -= 1
            ty += 1
        else:
            print "SE"
            tx += 1
            ty += 1
