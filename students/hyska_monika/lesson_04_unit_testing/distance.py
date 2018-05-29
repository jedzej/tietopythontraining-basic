# Program return distance between point A and B.
import math


def distance(x1, y1, x2, y2):
    try:
        if isinstance(x1, str) or isinstance(y1, str) or \
                isinstance(x2, str) or isinstance(y2, str):
            raise ValueError
        elif x1 is None or y1 is None or \
                x2 is None or y2 is None:
            raise TypeError
        vector = math.fabs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        vector = round(vector, 5)
        print("Length of vector is:", vector)
        return vector
    except ValueError:
        print("It isn't integer! Some parameter is string.")
        raise
    except TypeError:
        print("It isn't integer!. Some parameter is None")
        raise
