import bpy

class cls_jxsg_ExecutorPanel(bpy.types.Panel):
    
    bl_idname = "OBJECT_PT_jxsg_executor_panel"
    bl_label = "Generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "OBJECT_PT_jxsg_addon_general_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        settings = scene.jxsg_executor_settings
        
        layout.row().prop(settings, "cliff_base")
        layout.row().prop(settings, "cliff_height")
        layout.row().prop(settings, "base_radius")
        layout.row().prop(settings, "apex_radius")
        layout.row().prop(settings, "segments_on_meter")
        
        row = layout.row()
        row.column().label(text = "Height correction")
        row.column().prop(settings, "height_correction")
        
        row = layout.row()
        row.column().label(text = "Randomize")
        row.column().prop(settings, "height_correction_randomize")
        
        layout.row().column().prop(settings, "triangulate_faces")

        row = layout.row()
        row.scale_y = 2
        row.operator("object.jxsg_executor_operator")
