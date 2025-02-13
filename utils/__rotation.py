import bpy

import math
import random

class Rotation:

    def rotate(self, x, y, z):
        if x:
            self.rotate_by_axis_x(x)
        if y:
            self.rotate_by_axis_y(y)
        if z:
            self.rotate_by_axis_z(z)

    def random_rotation(self, k=360):
        self.rnd()
        x = random.randint(0, k * 2) - k
        y = random.randint(0, k * 2) - k
        z = random.randint(0, k * 2) - k
        self.rotate_by_axis_x(x)
        self.rotate_by_axis_y(y)
        self.rotate_by_axis_z(z)
        return (x, y, z)

    def rotate_by_axis_x(self, degree):
        bpy.ops.transform.rotate(
            value=math.radians(degree),
            orient_axis="X",
            orient_type='GLOBAL',
            orient_matrix=((1, -0, -0), (-0, 1, -0), (0, -0, 1)),
            orient_matrix_type='GLOBAL',
        )
    
    def rotate_by_axis_y(self, degree):
        bpy.ops.transform.rotate(
            value=math.radians(degree),
            orient_axis="Y",
            orient_type='GLOBAL',
            orient_matrix=((1, -0, -0), (-0, 1, -0), (0, -0, 1)),
            orient_matrix_type='GLOBAL',
        )
    
    def rotate_by_axis_z(self, degree):
        bpy.ops.transform.rotate(
            value=math.radians(degree),
            orient_axis="Z",
            orient_type='GLOBAL',
            orient_matrix=((1, -0, -0), (-0, 1, -0), (0, -0, 1)),
            orient_matrix_type='GLOBAL',
        )
