import helpers 

lines = helpers.read_input_at_once(__file__, 'char')

brak_state = {'(' : 'opening',
                '{' : 'opening',
                '[' : 'opening',
                '<' : 'opening',
                ')' : '(',
                '}' : '{',
                ']' : '[',
                '>' : '<'
}

brak_score = {')' : 3,
                ']' : 57,
                '}' : 1197,
                '>' : 25137
}

brack_stack = []
score = 0

for line in lines:
    for char in line:
        if brak_state[char] == 'opening':
            brack_stack.append(char)
        elif brak_state[char] == brack_stack[-1]:
                brack_stack.pop()
        else:
            score += brak_score[char]
            break

print(score)
