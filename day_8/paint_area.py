import math

def paint_calc(height, width, cover):
    return (math.ceil(height*width/cover))


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(f"The required number of cans is: {paint_calc(height=test_h, width=test_w, cover=coverage)}")