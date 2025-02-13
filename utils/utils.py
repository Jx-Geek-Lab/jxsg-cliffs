import bpy

import random
import string

from .__mesh import Mesh
from .__moving import Moving
from .__rotation import Rotation
from .__scaling import Scaling

class Utils(Mesh, Moving, Rotation, Scaling):
    
    def name(self, context, i):
        return context.scene.jxsg_main_settings.name_template.replace("*", "0" * (4 - len(str(i + context.scene.jxsg_main_settings.seek_index))) + str(i + context.scene.jxsg_main_settings.seek_index))
    
    def rnd(self):
        random.seed(''.join(random.choice(string.ascii_letters) for i in range(16)), version=2)
    
    def activate(self, name):
        for object in bpy.context.view_layer.objects:
            if object and object.name:
                if name == object.name:
                    object.select_set(True)
                    bpy.context.view_layer.objects.active = object
    
    def to_edit_mode(self):
        bpy.ops.object.mode_set(mode="EDIT")
    
    def to_object_mode(self):
        bpy.ops.object.mode_set(mode="OBJECT")
    
    def mode_vert(self):
        bpy.ops.mesh.select_mode(type='VERT')
    
    def mode_edge(self):
        bpy.ops.mesh.select_mode(type='EDGE')
    
    def mode_face(self):
        bpy.ops.mesh.select_mode(type='FACE')
    
    def begin(self, context):
        if context.scene.jxsg_main_settings.debug_mode:
            for object in bpy.data.objects:
                if object.name.startswith(context.scene.jxsg_main_settings.name_template.replace("*", "")):
                    bpy.data.objects.remove(object)
            for collection in context.scene.collection.children:
                context.scene.collection.children.unlink(collection)
    
    def end(self, context):
        if not context.scene.jxsg_main_settings.debug_mode:
            context.scene.jxsg_main_settings.seek_index = context.scene.jxsg_main_settings.seek_index + context.scene.jxsg_main_settings.number_of_generations
            context.scene.jxsg_main_settings.starting_position_by_axis_x = context.scene.jxsg_main_settings.starting_position_by_axis_x + context.scene.jxsg_main_settings.offset_on_step_by_axis_y
    
    def offset(self, context, i):
        settings = context.scene.jxsg_main_settings
        if "Matrix" == settings.positioning_method:
            x = settings.starting_position_by_axis_x + (i * settings.offset_on_step_by_axis_x)
            y = settings.starting_position_by_axis_y + (i * settings.offset_on_step_by_axis_y)
            z = settings.starting_position_by_axis_z + (i * settings.offset_on_step_by_axis_z)
            self.move(x, y, z)
        if "Circle" == settings.positioning_method:
            if settings.radius_compression:
                s = i * (settings.radius_compression / context.scene.jxsg_main_settings.number_of_generations)
                self.move_by_axis_y(settings.position_circle_radius + s)
            else:
                self.move_by_axis_y(settings.position_circle_radius)
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
            self.rotate_by_axis_z(i * settings.corner_step_in_degrees)
            bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
