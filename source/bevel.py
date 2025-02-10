import bpy


class OBJECT_OT_quickbevel(bpy.types.Operator):
    """Bevel"""
    bl_idname = "object.quickbevel"
    bl_label = "Quick Bevel"
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
    bl_label = "Quick Mirror"
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