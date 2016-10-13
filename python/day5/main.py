f = open('input.txt')
nice_lines = 0
vowel = ['a','e','i','o','u']

for line in f.readlines():
    is_nice_line = True
    for invalid in['ab', 'cd', 'pq', 'xy']:
        if invalid in line:
            is_nice_line = False

    if sum(1 for i in line if i in vowel) < 3:
        is_nice_line = False

    if sum(1 for index, v in enumerate(line) if (index+1) > len(line)-1 or line[index + 1] == v) == 1:
        is_nice_line = False

    if is_nice_line:
        nice_lines += 1

print nice_lines


