import bpy

class Scaling:

    def scale(self, value):
        bpy.ops.transform.resize(
            value=(value, value, value),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, True, True),
        )
    
    def scale_by_axis_x(self, value):
        bpy.ops.transform.resize(
            value=(value, 1, 1),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, False, False),
        )
    
    def scale_by_axis_y(self, value):
        bpy.ops.transform.resize(
            value=(1, value, 1),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, False),
        )
    
    def scale_by_axis_z(self, value):
        bpy.ops.transform.resize(
            value=(1, 1, value),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True),
        )
    
    def scale_not_by_axis_x(self, value):
        bpy.ops.transform.resize(
            value=(1, value, value),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, True),
        )
    
    def scale_not_by_axis_y(self, value):
        bpy.ops.transform.resize(
            value=(value, 1, value),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, False, True),
        )
    
    def scale_not_by_axis_z(self, value):
        bpy.ops.transform.resize(
            value=(value, value, 1),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(True, True, False),
        )
