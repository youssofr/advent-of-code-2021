import helpers

# read input and clean
readings = helpers.read_input_at_once(__file__)

only_encodings = lambda string : string.split('|')[0].split()
only_outputs = lambda string : string.split('|')[1].split()

encodings = list(map(only_encodings, readings))
readings = list(map(only_outputs, readings))

# variables to store answers
answer1 = 0 # part 1
answer2 = 0 # part 2

# going over each line
for reading in readings:
    for digit in reading:
        if 2 <= len(digit) <= 4 or len(digit) == 7:
            answer1 += 1

print(answer1)
print(answer2)