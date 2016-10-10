f = open('input.txt')
paper = 0
ribbon = 0

for line in f:
    l, w, h = map(int, line.split('x'))
    lw, wh, hl = [l*w, w*h, h*l]
    sq = 2 * (lw + wh + hl)
    low = min(lw, wh, hl)
    paper += sq + low

    extra_ribbon = [l, w, h]
    extra_ribbon.sort()
    first, second = extra_ribbon[:2]
    extra_ribbon = (first + first + second + second)
    ribbon += (l * w * h) + extra_ribbon

print "Paper: " + str(paper)
print "Ribbon: " + str(ribbon)
