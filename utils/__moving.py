import bpy

class Moving:

    def move(self, x, y, z):
        bpy.ops.transform.translate(
            value=(x, y, z),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, True, True),
        )
    
    def move_by_axis_x(self, value):
        bpy.ops.transform.translate(
            value=(value, 0, 0),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, False, False),
        )
    
    def move_by_axis_y(self, value):
        bpy.ops.transform.translate(
            value=(0, value, 0),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, False),
        )
    
    def move_by_axis_z(self, value):
        bpy.ops.transform.translate(
            value=(0, 0, value),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True),
        )
