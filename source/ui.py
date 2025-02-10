import bpy


class VIEW3D_PT_ddd_utils(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DDD'
    bl_label = 'Util'

    def draw(self, context):
        self.layout.operator('object.quickbevel')
        self.layout.operator('object.customcube')


class VIEW3D_PT_ddd_array(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DDD'
    bl_label = 'Array'
    
    def draw(self, context):
        self.layout.operator('object.array1d')
        self.layout.operator('object.array2d')
        self.layout.operator('object.array3d')