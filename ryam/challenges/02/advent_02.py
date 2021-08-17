# advent 02

## part 01
# CREATE: parse text function
def parse_line(line):
    # stolen from Ian
    return tuple(int(_int) for _int in line.split("x"))

# CREATE: surface area return function
def surface_area(_list):
    l = int(_list[0])
    w = int(_list[1])
    h = int(_list[2])
    sa_01 = l * w
    sa_02 = w * h
    sa_03 = h * l
    # find smallest value
    sa_list = [sa_01, sa_02, sa_03]
    sa_list.sort()
    # return total
    surfacearea = 2 * sa_01 + 2 * sa_02 + 2 * sa_03 + sa_list[0]
    return(surfacearea)

# CREATE: ribbon length return function
def ribbon_length(_list):
    l = int(_list[0])
    w = int(_list[1])
    h = int(_list[2])
    # find smallest value
    sa_list = [l, w, h]
    # sa_list.sort()
    # return total
    length = (sa_list[0]*2) + (sa_list[1]*2)
    length += sa_list[0] * sa_list[1] * sa_list[2]
    return(length)

# examples
ex_01_str = '2x3x4'
ex_02_str = '1x1x10'
ex_01 = parse_line(ex_01_str)
ex_02 = parse_line(ex_02_str)
print('ex 01 - wrapper:', surface_area(ex_01))
print('ex 02 - wrapper:', surface_area(ex_02))
print('ex 01 - ribbon:', ribbon_length(ex_01))
print('ex 02 - ribbon:', ribbon_length(ex_02))

# size of input
input_size = 0
with open('ryam/challenges/02/input.txt') as f:
    for line in f:
        input_size = input_size + 1

# open input
input = open("ryam/challenges/02/input.txt", "r")

# loop for answer 01 + 02
answer_01 = 0
answer_02 = 0
i = 0
while i != 1000:
    input_line = input.readline()
    input_line = parse_line(input_line) 
    answer_01 += surface_area(input_line)
    answer_02 += ribbon_length(input_line)
    print(answer_02)
    i += 1

print("Part 01:", answer_01)
print("Part 02:", answer_02)