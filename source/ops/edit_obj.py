# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


class OBJECT_OT_resetobj(bpy.types.Operator):
    """Resets the selected object's transform"""
    bl_idname = "object.resetobj"
    bl_label = "Reset Transform"
    bl_options = { 'REGISTER', 'UNDO' }

    clear_delta: bpy.props.BoolProperty(name='Clear Delta', default=True)

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D"
    
    def execute(self, context):
        bpy.ops.object.location_clear(clear_delta=self.clear_delta)
        bpy.ops.object.rotation_clear(clear_delta=self.clear_delta)
        bpy.ops.object.scale_clear(clear_delta=self.clear_delta)

        return { 'FINISHED' }