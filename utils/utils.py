import bpy

import random
import string

from .__moving import Moving
from .__rotation import Rotation
from .__scaling import Scaling

class Utils(Moving, Rotation, Scaling):

    def randomize(self):
        random.seed(''.join(random.choice(string.ascii_letters) for i in range(16)), version=2)

    def activate(self, name):
        for object in bpy.context.view_layer.objects:
            if object and object.name:
                if name == object.name:
                    object.select_set(True)
                    bpy.context.view_layer.objects.active = object
    
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
