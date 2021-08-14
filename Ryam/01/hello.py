# Advent 01

# input variables
f = open("01/advent_01_input.txt", "r") # open input file
input = f.read()                     # store string
size = len(input)                    # store string length

# puzzle variables
a = '('
b = ')'
basement = -1

# answer variables
answer_1 = 0
answer_2 = 0

# loop variables
i = 0
part_2 = False

while i < size:

    #determine character
    char = input[i]

    # increase on (
    if char == a:
        answer_1 += 1

    # decrease on )
    if char == b:
        answer_1 -= 1

    # increment loop    
    i += 1
    
    # find answer_2
    if answer_1 == basement & part_2 == False:
        answer_2 = i + 1 # adjust for i = 0 (?)
        part_2 = True    # prevent multiple answers

# print answers
print('part 1:', answer_1)
print('part 2', answer_2)