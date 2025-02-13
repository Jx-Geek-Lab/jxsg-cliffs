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
                
        row = layout.row()
        row.scale_y = 2
        row.operator("object.jxsg_executor_operator")
