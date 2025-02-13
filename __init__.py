import bpy

from .executor.settings import cls_jxsg_ExecutorGroup
from .executor.operator import cls_jxsg_ExecutorOperator
from .executor.panel import cls_jxsg_ExecutorPanel

default_debug_mode = True
default_name_template = "O_Mesh.*"
default_number_of_generations = 5
default_seek_index = 0
default_positioning_method = "Matrix"
default_starting_position_by_axis_x = 0.0
default_starting_position_by_axis_y = 0.0
default_starting_position_by_axis_z = 0.0
default_offset_on_step_by_axis_x = 0.0
default_offset_on_step_by_axis_y = 5.0
default_offset_on_step_by_axis_z = 0.0
default_position_circle_radius = 5.0
default_corner_step_in_degrees = 45.0
default_radius_compression = 0.0

class cls_jxsg_MainSettingsGroup(bpy.types.PropertyGroup):
    debug_mode: bpy.props.BoolProperty(default=default_debug_mode, name=" Debug mode")
    name_template: bpy.props.StringProperty(default=default_name_template, name="")
    number_of_generations: bpy.props.IntProperty(default=default_number_of_generations, min=1, max=100, name="")
    seek_index: bpy.props.IntProperty(default=default_seek_index, min=0, max=1000, name="")
    positioning_method: bpy.props.EnumProperty(
        default = default_positioning_method,
        items = [
            ("Matrix", "Matrix", "Matrix", "Matrix", 1),
            ("Circle", "Circle", "Circle", "Circle", 2),
        ],
        name = ""
    )
    starting_position_by_axis_x: bpy.props.FloatProperty(default=default_starting_position_by_axis_x, min=-100.0, max=100.0, name="X")
    starting_position_by_axis_y: bpy.props.FloatProperty(default=default_starting_position_by_axis_y, min=-100.0, max=100.0, name="Y")
    starting_position_by_axis_z: bpy.props.FloatProperty(default=default_starting_position_by_axis_z, min=-100.0, max=100.0, name="Z")
    offset_on_step_by_axis_x: bpy.props.FloatProperty(default=default_offset_on_step_by_axis_x, min=-10.0, max=10.0, name="X")
    offset_on_step_by_axis_y: bpy.props.FloatProperty(default=default_offset_on_step_by_axis_y, min=-10.0, max=10.0, name="Y")
    offset_on_step_by_axis_z: bpy.props.FloatProperty(default=default_offset_on_step_by_axis_z, min=-10.0, max=10.0, name="Z")
    position_circle_radius: bpy.props.FloatProperty(default=default_position_circle_radius, min=0.5, max=50.0, name="")
    corner_step_in_degrees: bpy.props.FloatProperty(default=default_corner_step_in_degrees, min=1.0, max=360.0, name="")
    radius_compression: bpy.props.FloatProperty(default=default_radius_compression, min=-25.0, max=25.0, name="")

class cls_jxsg_MainSettingsOperator(bpy.types.Operator):
    
    bl_idname = "object.jxsg_main_settings_operator"
    bl_label = "Drop to default"

    def execute(self, context):
        
        scene = context.scene
        settings = scene.jxsg_main_settings
        
        settings.debug_mode=default_debug_mode
        settings.name_template=default_name_template
        settings.number_of_generations=default_number_of_generations
        settings.seek_index=default_seek_index
        settings.positioning_method=default_positioning_method
        settings.starting_position_by_axis_x=default_starting_position_by_axis_x
        settings.starting_position_by_axis_y=default_starting_position_by_axis_y
        settings.starting_position_by_axis_z=default_starting_position_by_axis_z
        settings.offset_on_step_by_axis_x=default_offset_on_step_by_axis_x
        settings.offset_on_step_by_axis_y=default_offset_on_step_by_axis_y
        settings.offset_on_step_by_axis_z=default_offset_on_step_by_axis_z
        settings.position_circle_radius=default_position_circle_radius
        settings.corner_step_in_degrees=default_corner_step_in_degrees
        settings.radius_compression=default_radius_compression
        
        return {'FINISHED'}

class cls_jxsg_AddonGeneralPanel(bpy.types.Panel):
    
    bl_idname = "OBJECT_PT_jxsg_addon_general_panel"
    bl_label = "JX Smart Generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "JXSG"

    def draw(self, context):
        pass

class cls_jxsg_MainSettingsPanel(bpy.types.Panel):
    
    bl_idname = "OBJECT_PT_jxsg_main_settings_panel"
    bl_label = "Main settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "OBJECT_PT_jxsg_addon_general_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        settings = scene.jxsg_main_settings
        
        layout.row().prop(settings, "debug_mode")
        
        row = layout.row()
        row.column().label(text = "Name template")
        row.column().prop(settings, "name_template")
        
        row = layout.row()
        row.column().label(text = "Number of generations")
        row.column().prop(settings, "number_of_generations")
        
        row = layout.row()
        row.column().label(text = "Seek index")
        row.column().prop(settings, "seek_index")
        
        row = layout.row()
        row.column().label(text = "Positioning method")
        row.column().prop(settings, "positioning_method")
        
        if "Matrix" == settings.positioning_method:
        
            layout.row().label(text = "Starting position by axis")
            row = layout.row()
            row.column().prop(settings, "starting_position_by_axis_x")
            row.column().prop(settings, "starting_position_by_axis_y")
            row.column().prop(settings, "starting_position_by_axis_z")
            
            layout.row().label(text = "Offset on step by axis")
            row = layout.row()
            row.column().prop(settings, "offset_on_step_by_axis_x")
            row.column().prop(settings, "offset_on_step_by_axis_y")
            row.column().prop(settings, "offset_on_step_by_axis_z")
        
        if "Circle" == settings.positioning_method:
            
            row = layout.row()
            row.column().label(text = "Position circle radius")
            row.column().prop(settings, "position_circle_radius")
            
            row = layout.row()
            row.column().label(text = "Corner step in degrees")
            row.column().prop(settings, "corner_step_in_degrees")
            
            row = layout.row()
            row.column().label(text = "Radius compression")
            row.column().prop(settings, "radius_compression")
        
        row = layout.row()
        row.scale_y = 2
        row.operator("object.jxsg_main_settings_operator")

__classes = [
    cls_jxsg_MainSettingsGroup,
    cls_jxsg_ExecutorGroup,
    cls_jxsg_MainSettingsOperator,
    cls_jxsg_ExecutorOperator,
    cls_jxsg_AddonGeneralPanel,
    cls_jxsg_MainSettingsPanel,
    cls_jxsg_ExecutorPanel,
]

def register():
    
    for cls in __classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.jxsg_main_settings = bpy.props.PointerProperty(type=cls_jxsg_MainSettingsGroup)
    bpy.types.Scene.jxsg_executor_settings = bpy.props.PointerProperty(type=cls_jxsg_ExecutorGroup)

def unregister():
    
    for cls in __classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
