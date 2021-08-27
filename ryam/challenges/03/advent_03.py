# Update Position
def movement(DIR, POS):
    if DIR == '>':
        X        = POS[0] + 1
        Y        = POS[1]
    if DIR == '<':
        X        = POS[0] - 1
        Y        = POS[1]
    if DIR == '^':
        X        = POS[0]
        Y        = POS[1] - 1    
    if DIR == 'v':
        X        = POS[0]
        Y        = POS[1] + 1  
    POS = (X, Y)
    return(POS)

# check if already visited
def check(POS, LIST):
    check_index = 0
    check_size = len(LIST)
    while check_index < check_size:
        if LIST[check_index] == POS:
            return False
        else:
            check_index += 1
        return True

# run map
def journey(MAP):
    position   = (0, 0)
    tracker    = [position]
    deliveries = 1
    size = len(MAP)
    i = 0
    while i < size:
        char = MAP[i]
        position = movement(char, position)
        check_delivery = check(position, tracker)
        if check_delivery == True:
            deliveries += 1
            tracker += [position]
            i += 1
        else:
            i += 1
    return(deliveries)

# test examples
ex1 = '>'
ex2 = '^>v<'
ex3 = '^v^v^v^v^v'

print('Example 1:', journey(ex1))
print('Example 2:', journey(ex2))
print('Example 3:', journey(ex3))