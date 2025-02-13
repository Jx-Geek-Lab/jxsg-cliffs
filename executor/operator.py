import bpy

from .executor import Executor

class cls_jxsg_ExecutorOperator(bpy.types.Operator):
    
    bl_idname = "object.jxsg_executor_operator"
    bl_label = "Start"

    def execute(self, context):
        
        Executor().run(context)
        
        return {'FINISHED'}
