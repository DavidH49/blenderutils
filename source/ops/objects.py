import bpy
from .. import util


class OBJECT_OT_corncube(bpy.types.Operator):
    bl_idname = "mesh.primitive_corncube_add"
    bl_label = "Corner Cube"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        util.construct_cube((1, 1, 1))
        return { 'FINISHED' }


class OBJECT_OT_botcube(bpy.types.Operator):
    bl_idname = "mesh.primitive_bottomcube_add"
    bl_label = "Bottom Cube" #🥺👉👈
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        util.construct_cube((0, 0, 1))
        return { 'FINISHED' }


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_corncube.bl_idname, icon='MESH_CUBE')
    self.layout.operator(OBJECT_OT_botcube.bl_idname, icon='MESH_CUBE')