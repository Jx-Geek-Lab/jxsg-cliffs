import bpy

class cls_jxsg_ExecutorGroup(bpy.types.PropertyGroup):
    version: bpy.props.IntProperty(default=1, min=1, max=100, name="Version")
