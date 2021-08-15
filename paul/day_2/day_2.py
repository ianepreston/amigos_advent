from os import walk


with open(r'day_2\input.txt', 'r') as f:
    packages = f.readlines()

paper_footage = 0
ribbon_footage = 0

for p in packages:
    dimensions = [int(d) for d in p.split('x')]
    width = dimensions[0]
    length = dimensions[1]
    height = dimensions[2]

    wl = width * length
    wh = width * height
    lh = length * height

    #paper
    area = (2 * wl) + (2 * wh) + (2 * lh)
    min_surface = min(wl, wh, lh)

    paper_footage += area + min_surface

    #ribbon
    sorted_dimensions = sorted(dimensions)
    ribbon_wrap = 2 * (sorted_dimensions[0] +  sorted_dimensions[1])
    ribbon_bow = width * length * height

    ribbon_footage += ribbon_wrap + ribbon_bow
        
print (paper_footage)
print (ribbon_footage)

    

