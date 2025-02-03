import bpy
P = bpy.props
U = bpy.utils
O = bpy.ops


class OBJECT_OT_array1d(bpy.types.Operator):
    """Arrays the object on the X axis"""
    bl_idname = "object.array1d"
    bl_label = "Add Array 1D"
    bl_options = { 'REGISTER', 'UNDO' }

    count: P.IntProperty(name='Count', default=2, min=1)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        try:
            O.object.modifier_add(type='ARRAY')

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
    
    count_x: P.IntProperty(name='Count X', default=2, min=1)
    count_y: P.IntProperty(name='Count Y', default=2, min=1)
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' 
    
    def execute(self, context):
        try:
            O.object.modifier_add(type='ARRAY')
            O.object.modifier_add(type='ARRAY')
            
            active = context.active_object
            
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

    count_x: P.IntProperty(name='Count X', default=2, min=1)
    count_y: P.IntProperty(name='Count Y', default=2, min=1)
    count_z: P.IntProperty(name='Count Z', default=2, min=1)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        try:
            O.object.modifier_add(type='ARRAY')
            O.object.modifier_add(type='ARRAY')
            O.object.modifier_add(type='ARRAY')

            active = context.active_object

            active.modifiers[-2].relative_offset_displace = (0, 1, 0)
            active.modifiers[-1].relative_offset_displace = (0, 0, 1)
            active.modifiers[-3].count = self.count_x
            active.modifiers[-2].count = self.count_y
            active.modifiers[-1].count = self.count_z
        
        except RuntimeError:
            pass

        return { 'FINISHED' }