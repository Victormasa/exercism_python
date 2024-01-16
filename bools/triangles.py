def equilateral(sides):
    try:
        sides.index(0)
        return False
    except ValueError:
        pass
        if sides[0] == sides[1] and sides[0] == sides[2]:
            return True
        else:
            return False


def isosceles(sides):
    pass


def scalene(sides):
    pass

sides = [2,2,2]
#print ()

