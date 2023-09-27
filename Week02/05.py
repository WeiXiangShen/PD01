
def triangle():
    side = [int(input()) for i in range(3)]

    side.sort()

    if side[0] + side[1] <= side[2]:
        print("not a triangle")
    elif side[0] == side[2]:
        print("equilateral triangle")
    elif side[0] == side[1] or side[1] == side[2]:
        print("isosceles triangle")
    elif side[0]**2 + side[1]**2 < side[2]**2:
        print("obtuse triangle")
    elif side[0]**2 + side[1]**2 > side[2]**2:
        print("acute triangle")
    elif side[0]**2 + side[1]**2 == side[2]**2:
        print("right triangle")


triangle()