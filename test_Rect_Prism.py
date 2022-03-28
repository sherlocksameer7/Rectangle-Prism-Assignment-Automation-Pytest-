import math
import Rect_Prism


def test_surface_area():
    l = 10
    b = 20
    h = 30
    result = Rect_Prism.surfacearea(l, b, h)
    assert result == 2 * (l * b + b * h + h * l)



def test_volume():
    l = 10
    b = 20
    h = 30
    result = Rect_Prism.volume(l, b, h)


    assert result == l * b * h

def test_space():
    l = 10
    b = 20
    h = 30
    result = Rect_Prism.space_diagonal(l, b, h)
    assert result == math.sqrt(l * 2 + b * 2 + h * 2)