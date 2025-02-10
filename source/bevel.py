import bpy
from . import util


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


class OBJECT_OT_customcube(bpy.types.Operator):
    """Construct a cube with a custom origin"""
    bl_idname = "object.customcube"
    bl_label = "Construct Cube"
    bl_options = { 'REGISTER', 'UNDO' }

    location: bpy.props.FloatVectorProperty(name='Location', default=(0, 0, 0))

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D"
    
    def execute(self, context):
        try:
            util.construct_cube(self.location)
        except RuntimeError:
            pass

        return { 'FINISHED' }
