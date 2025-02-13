import bpy

import random

from ..utils.utils import Utils

utils = Utils()

class Executor:
    
    def do(self, context, i):
        scene = context.scene
        task = scene.jxsg_executor_settings
        
        utils.rnd()
        object = utils.add_circle(utils.name(context, i), task.cliff_base, task.base_radius)
        utils.to_edit_mode()
        if task.hard_randomize:
            utils.randomize(0.1, 0.5)
        height = task.cliff_height
        if task.height_correction:
            height = height + ((task.height_correction * random.uniform(task.height_correction_randomize, 1)) * i)
        utils.extrude(0, 0, height)
        utils.scale_not_by_axis_z(task.apex_radius)
        utils.randomize(0.075, 0.1)
        utils.mode_vert()
        utils.scale_by_axis_z(0)
        utils.add_face()
        bpy.ops.mesh.inset(thickness=0.1, depth=0)
        bpy.ops.transform.translate(value=(0, 0, 0.073731), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        bpy.ops.mesh.select_more()
        if task.segments_on_meter - 1:
            utils.loopcat(task.segments_on_meter - 1)
        utils.mode_vert()
        utils.randomize(0.075, 0.1)
        if task.triangulate_faces:
            bpy.ops.mesh.select_more()
            utils.triangulate()
        utils.select(object.data.vertices, 0, task.cliff_base - 1)
        utils.scale_by_axis_z(0)
        utils.add_face()
        utils.to_object_mode()
        utils.offset(context, i)

    def run(self, context):
        
        utils.begin(context)
        
        for i in range(context.scene.jxsg_main_settings.number_of_generations):
            self.do(context, i)
        
        utils.end(context)
