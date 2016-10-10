from sets import Set

f = open('input.txt')
content = list(f.read())
last_position = (0, 0)
path = Set([])

for instruction in content:

    if instruction == '^':
        last_position = (last_position[0], last_position[1]+1)
    elif instruction == '>':
        last_position = (last_position[0] + 1, last_position[1])
    elif instruction == 'v':
        last_position = (last_position[0], last_position[1] - 1)
    elif instruction == '<':
        last_position = (last_position[0] - 1, last_position[1])

    path.add(last_position)

print len(path) + 1

