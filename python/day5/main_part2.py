f = open('input.txt')
nice_lines = 0

for line in f.readlines():
    is_nice_line = True

    if sum(1 for index, v in enumerate(line) if (index+2) <= len(line)-1 and line[index + 2] == v) == 0:
        is_nice_line = False

    if sum(1 for index, v in enumerate(line) if (index+3) <= len(line)-1 and v + line[index+1] in line[:index+1]) == 0:
        is_nice_line = False


    if is_nice_line:
        print line
        nice_lines += 1

print nice_lines


