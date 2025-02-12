# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from . import add_obj


class VIEW3D_PT_ddd_panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = 'DDD - Util'
    
    def draw(self, context):
        layout = self.layout

        layout.operator('object.resetobj')

        layout.separator()

        layout.operator('object.quickbevel')
        layout.operator('object.quickmirror')

        layout.separator()

        layout.operator('object.array1d')
        layout.operator('object.array2d')
        layout.operator('object.array3d')


def objects_menu(self, context):
    layout = self.layout

    layout.separator()
    layout.operator(add_obj.OBJECT_OT_corncube.bl_idname, icon='MESH_CUBE')
    layout.operator(add_obj.OBJECT_OT_edgecube.bl_idname, icon='MESH_CUBE')
    layout.operator(add_obj.OBJECT_OT_botcube.bl_idname, icon='MESH_CUBE')