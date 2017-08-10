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
            tx += 1
            print 'E'
        else:
            tx -= 1
            print 'W'
    elif ty > y:
        if tx == x:
            ty -= 1
            print 'N'
        elif tx > x:
            tx -= 1
            ty -= 1
            print 'NW'
        else:
            tx += 1
            ty -= 1
            print 'NE'
    elif ty < y:
        if tx == x:
            ty += 1
            print 'S'
        elif tx > x:
            tx -= 1
            ty += 1
            print 'SW'
        else:
            tx += 1
            ty += 1
            print 'SE'
