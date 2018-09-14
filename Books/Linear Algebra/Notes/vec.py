#!/usr/bin/env python
from math import *
import sys

# # Magnitude and angle of vector 1
# mag_1 = int(sys.argv[1])
# ang_1 = int(sys.argv[2])

# # Magnitude and angle of vector 2
# mag_2 = int(sys.argv[3])
# ang_2 = int(sys.argv[4])


def angle_mag(mag_1, ang_1, mag_2, ang_2):
  """  
  This function is meant to return the magnitude and angle direction
  of the vector derived from adding vectors 1 and 2

  Args:
    mag_1, ang_1 : magnitude and angle of vector 1
    mag_2, ang_2 : magnitude and angle of vector 2

  Methods:
    cos(x): returns the cosine of x in radians
    sin(x): returns the sine of x in radians
    radians(x): takes in a degree x and returns radians
    hypot(x, y): returns the length of a vector from origin to point(x, y) ie. sqrt(x*x, y*y)
    degrees(): returns the a degree from radians
    atan2(): takes in the points x and y and returns the angle in the correct quadrant.

  """
  # Stores the x cordinate for our new vector
  x_component = mag_1*cos(radians(ang_1)) + mag_2*cos(radians(ang_2))
  # Stores the y cordinate for our new vector
  y_component = mag_1*sin(radians(ang_1)) + mag_2*sin(radians(ang_2))

  # Storing the magnitude/ length of our new vector
  new_mag = hypot(x_component, y_component)

  # Stores the angle of our new vector. Note that we begin with y
  new_ang = degrees(atan2(y_component, x_component))
  #  returns the positive angle made with the x-axis
  if new_ang < 0:
    new_ang = 360 + new_ang

  print(f"It is {isinstance(mag_1, int)}. {mag_1} is a of type {type(mag_1).__name__}.")

  print(f"New magnitude: {new_mag}\nNew angle: {new_ang}")

def test():
  print("Sup bruv")

options = {
  "1": angle_mag,
  "2": test,
}

option, parameters = sys.argv[0], sys.argv[1:]
options[option](*parameters)