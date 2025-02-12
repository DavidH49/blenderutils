# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


class OBJECT_OT_array1d(bpy.types.Operator):
    """Arrays the object on the X axis"""
    bl_idname = "object.array1d"
    bl_label = "Add Array 1D"
    bl_options = { 'REGISTER', 'UNDO' }

    count: bpy.props.IntProperty(name='Count', default=2, min=1)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        try:
            bpy.ops.object.modifier_add(type='ARRAY')

            active = context.active_object
            active.modifiers[-1].count = self.count
        
        except RuntimeError:
            pass

        return { 'FINISHED' }


class OBJECT_OT_array2d(bpy.types.Operator):
    """Arrays the object on the X and Y axis"""
    bl_idname = "object.array2d"
    bl_label = "Add Array 2D"
    bl_options = { 'REGISTER', 'UNDO' }
    
    count_x: bpy.props.IntProperty(name='Count X', default=2, min=1)
    count_y: bpy.props.IntProperty(name='Count Y', default=2, min=1)
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' 
    
    def execute(self, context):
        try:
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.ops.object.modifier_add(type='ARRAY')
            
            active = context.active_object
            
            active.modifiers[-2].name = 'Array X'
            active.modifiers[-1].name = 'Array Y'
            active.modifiers[-1].relative_offset_displace = (0, 1, 0)
            active.modifiers[-2].count = self.count_x
            active.modifiers[-1].count = self.count_y
            
        except RuntimeError:
            pass
        
        return { 'FINISHED' }


class OBJECT_OT_array3d(bpy.types.Operator):
    """Arrays the object on all three axis"""
    bl_idname = "object.array3d"
    bl_label = "Add Array 3D"
    bl_options = { 'REGISTER', 'UNDO' }

    count_x: bpy.props.IntProperty(name='Count X', default=2, min=1)
    count_y: bpy.props.IntProperty(name='Count Y', default=2, min=1)
    count_z: bpy.props.IntProperty(name='Count Z', default=2, min=1)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        try:
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.ops.object.modifier_add(type='ARRAY')

            active = context.active_object

            active.modifiers[-3].name = 'Array X'
            active.modifiers[-2].name = 'Array Y'
            active.modifiers[-1].name = 'Array Z'
            active.modifiers[-2].relative_offset_displace = (0, 1, 0)
            active.modifiers[-1].relative_offset_displace = (0, 0, 1)
            active.modifiers[-3].count = self.count_x
            active.modifiers[-2].count = self.count_y
            active.modifiers[-1].count = self.count_z
        
        except RuntimeError:
            pass

        return { 'FINISHED' }


class OBJECT_OT_quickbevel(bpy.types.Operator):
    """Bevel"""
    bl_idname = "object.quickbevel"
    bl_label = "Add Bevel"
    bl_options = { 'REGISTER', 'UNDO' }

    width: bpy.props.FloatProperty(name='Amount', default=0.1, min=0)
    segments: bpy.props.IntProperty(name='Segments', default=1, min=1)

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D"
    
    def execute(self, context):
        try:
            bpy.ops.object.modifier_add(type='BEVEL')
            active = context.active_object

            active.modifiers[-1].width = self.width
            active.modifiers[-1].segments = self.segments
        
        except RuntimeError:
            pass
        
        return { 'FINISHED' }


class OBJECT_OT_quickmirror(bpy.types.Operator):
    """Mirror"""
    bl_idname = "object.quickmirror"
    bl_label = "Add Mirror"
    bl_options = { 'REGISTER', 'UNDO' }

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D"
    
    def execute(self, context):
        try:
            bpy.ops.object.modifier_add(type='MIRROR')
        
        except RuntimeError:
            pass

        return { 'FINISHED' }