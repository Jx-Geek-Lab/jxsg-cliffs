import bpy

class cls_jxsg_ExecutorGroup(bpy.types.PropertyGroup):
    version: bpy.props.IntProperty(default=1, min=1, max=100, name="Version")
    cliff_base: bpy.props.IntProperty(default=5, min=5, max=15, name="Cliff segments base")
    cliff_height: bpy.props.FloatProperty(default=1.0, min=1.0, max=25.0, name="Cliff apex height")
    base_radius: bpy.props.FloatProperty(default=2.0, min=1.0, max=10.0, name="Base radius")
    apex_radius: bpy.props.FloatProperty(default=1.5, min=0.1, max=2.0, name="Apex radius")
    segments_on_meter: bpy.props.IntProperty(default=1, min=1, max=10, name="Segments count")
    height_correction: bpy.props.FloatProperty(default=0.0, min=-5.0, max=5.0, name="")
    height_correction_randomize: bpy.props.FloatProperty(default=1.0, min=0.1, max=1.0, name="")
    height_correction_randomize: bpy.props.FloatProperty(default=1.0, min=0.1, max=1.0, name="")
    triangulate_faces: bpy.props.BoolProperty(default=False, name=" Triangulate faces")
