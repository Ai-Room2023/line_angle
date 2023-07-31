import math
from collections import namedtuple
import numpy as np
import cv2


# Start coordinate, here.
p1 = [256, 10]
# End coordinate, here.
#p2 = [512, 256]
p2 = [80, 510]

def get_angle():
    """Get the angle of this line with the vertical axis."""
    dy = abs(p2[0] - p1[0])
    dx = abs(p2[1] - p1[1])
    theta = math.atan2(dy, dx)
    angle = math.degrees(theta)  # angle is in (-180, 180]
    #if angle < 0:
    #    angle = 360 + angle
    return angle
res = get_angle()
print(res)
