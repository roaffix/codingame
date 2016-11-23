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
