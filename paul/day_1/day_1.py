with open(r'day_1\input.txt', 'r') as f:
    directions = f.read()

location = 0
basement = 0
for count, direction in enumerate(directions):
    if direction == '(':
        location +=1
    if direction == ')':
        location -=1

    if location < 0 and basement == 0:
        basement = count + 1

print (location)
print (basement)