# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from . import objects
from . import obj


class VIEW3D_PT_ddd_utils(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DDD'
    bl_label = 'Util'

    def draw(self, context):
        self.layout.operator('object.resetobj')
        self.layout.operator('object.quickbevel')
        self.layout.operator('object.quickmirror')


class VIEW3D_PT_ddd_array(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DDD'
    bl_label = 'Array'
    
    def draw(self, context):
        self.layout.operator('object.array1d')
        self.layout.operator('object.array2d')
        self.layout.operator('object.array3d')


def objects_menu(self, context):
    self.layout.operator(objects.OBJECT_OT_corncube.bl_idname, icon='MESH_CUBE')
    self.layout.operator(objects.OBJECT_OT_botcube.bl_idname, icon='MESH_CUBE')