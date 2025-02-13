import bpy

import random

class Mesh:
    
    def add_face(self):
        bpy.ops.mesh.edge_face_add()
    
    def add_circle(self, name, v, r):
        bpy.ops.mesh.primitive_circle_add(
            vertices=v,
            radius=r,
            align='WORLD',
            location=(0, 0, 0),
            scale=(1, 1, 1),
        )
        bpy.context.active_object.name = name
        return bpy.context.active_object
    
    def select_all(self):
        bpy.ops.mesh.select_all(action='SELECT')
    
    def deselect_all(self):
        bpy.ops.mesh.select_all(action='DESELECT')
    
    def loopcat(self, c):
        bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":c, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":23, "mesh_select_mode_init":(False, True, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "correct_uv":True, "release_confirm":False, "use_accurate":False})
    
    def triangulate(self):
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
    
    def randomize(self, f, t, u=0, n=0):
        bpy.ops.transform.vertex_random(offset=random.uniform(f, t), uniform=u, normal=n, seed=random.randint(1, 500))
    
    def select(self, e, f, t):
        self.to_edit_mode()
        self.deselect_all()
        self.mode_vert()
        self.to_object_mode()
        for i in range(len(e)):
            e[i].select = i >= f and i <= t
        self.to_edit_mode()
    
    def extrude(self, x, y, z):
        bpy.ops.mesh.extrude_region_move(
            MESH_OT_extrude_region={
                "use_normal_flip":False,
                "use_dissolve_ortho_edges":False,
                "mirror":False},
            TRANSFORM_OT_translate={
                "value":(x, y, z),
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(bool(x), bool(y), bool(z)),
            },
        )

    def normals_flip(self):
        bpy.ops.mesh.flip_normals()

    def normals_consistent_outside(self):
        bpy.ops.mesh.normals_make_consistent(inside=False)
    
    def normals_consistent_inside(self):
        bpy.ops.mesh.normals_make_consistent(inside=True)
