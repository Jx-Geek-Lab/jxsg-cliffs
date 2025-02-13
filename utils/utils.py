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
