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

brak_score = {  '(' : 1,
                '[' : 2,
                '{' : 3,
                '<' : 4
}

scores = []

for line in lines:
    brack_stack = []
    curropt = False
    for char in line:
        if brak_state[char] == 'opening':
            brack_stack.append(char)
        elif brak_state[char] == brack_stack[-1]:
                brack_stack.pop()
        else:
            curropt = True
            break

    if not curropt:
        line_score = 0
        brack_stack.reverse()
        for brack in brack_stack:
            line_score *= 5 
            line_score += brak_score[brack]
        scores.append(line_score)
    
print(sorted(scores)[len(scores)//2])
