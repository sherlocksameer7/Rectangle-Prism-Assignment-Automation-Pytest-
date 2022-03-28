import math


def surfacearea(l, b, h):
    return 2 * (l * b + b * h + h * l)


def volume(l, b, h):
    return l * b * h


def space_diagonal(l, b, h):
    return math.sqrt(l * 2 + 2 * b + h * 2)


if __name__ == "__main__":

    l = int(input("Enter the length : "))
    b = int(input("Enter the breadth : "))
    h = int(input("Enter the height : "))

    area = surfacearea(l, b, h)
    vol = volume(l, b, h)
    space = space_diagonal(l, b, h)

    print("The surface area is ", area)
    print("The volume is ", vol)
    print("The space diagonal is ", space)