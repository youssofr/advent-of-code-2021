import helpers

# read input and clean for relevant portion of the string
readings = helpers.read_input_at_once(__file__)

only_outputs = lambda string : string.split('|')[1].split()

readings = list(map(only_outputs, readings))

# variables to store answers
answer = 0 # part 1

# going over each line to count "easy digits"
for reading in readings:
    for digit in reading:
        if 2 <= len(digit) <= 4 or len(digit) == 7:
            answer += 1

print(answer)