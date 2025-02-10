import bpy
from . import util
from . import meshes


class OBJECT_OT_corncube(bpy.types.Operator):
    bl_idname = "mesh.primitive_corncube_add"
    bl_label = "Corner Cube"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        util.deselect_all()

        mesh = meshes.MESH_CORNCUBE
        mesh_data = util.construct_mesh_data("corncube", mesh.verts, mesh.edges, mesh.faces)
        mesh_obj = util.construct_mesh_obj(self.bl_label, mesh_data)

        util.select_mesh(mesh_obj)
        util.recalc_normals()

        return { 'FINISHED' }


class OBJECT_OT_botcube(bpy.types.Operator):
    bl_idname = "mesh.primitive_bottomcube_add"
    bl_label = "Bottom Cube" #🥺👉👈
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        util.deselect_all()

        mesh = meshes.MESH_BOTTOMCUBE
        mesh_data = util.construct_mesh_data("botcube", mesh.verts, mesh.edges, mesh.faces)
        mesh_obj = util.construct_mesh_obj(self.bl_label, mesh_data)

        util.select_mesh(mesh_obj)
        util.recalc_normals()

        return { 'FINISHED' }


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_corncube.bl_idname, icon='MESH_CUBE')
    self.layout.operator(OBJECT_OT_botcube.bl_idname, icon='MESH_CUBE')