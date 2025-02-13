import bpy

from ..utils.utils import Utils

utils = Utils()

class Executor:
    
    def do(self, context, i):
        pass

    def run(self, context):
        
        utils.begin(context)
        
        for i in range(context.scene.jxsg_main_settings.number_of_generations):
            self.do(context, i)
        
        utils.end(context)
