# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    "name": "DDDs Blenderutils",
    "author": "DDD",
    "description": "",
    "blender": (4, 2, 2),
    "version": (1, 3, 0),
    "location": "",
    "warning": "",
    "category": "Generic",
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(bevel)
    importlib.reload(array)
    importlib.reload(objects)
    importlib.reload(util)
else:
    from . import ui
    from . import bevel
    from . import array
    from . import objects
    from . import util

import bpy


def register():
    bpy.utils.register_class(ui.VIEW3D_PT_ddd_utils)
    bpy.utils.register_class(ui.VIEW3D_PT_ddd_array)
    bpy.utils.register_class(bevel.OBJECT_OT_quickbevel)
    bpy.utils.register_class(array.OBJECT_OT_array1d)
    bpy.utils.register_class(array.OBJECT_OT_array2d)
    bpy.utils.register_class(array.OBJECT_OT_array3d)
    bpy.utils.register_class(objects.OBJECT_OT_corncube)
    bpy.utils.register_class(objects.OBJECT_OT_botcube)

    bpy.types.VIEW3D_MT_mesh_add.append(objects.menu_func)


def unregister():
    bpy.utils.unregister_class(ui.VIEW3D_PT_ddd_utils)
    bpy.utils.unregister_class(ui.VIEW3D_PT_ddd_array)
    bpy.utils.unregister_class(bevel.OBJECT_OT_quickbevel)
    bpy.utils.unregister_class(array.OBJECT_OT_array1d)
    bpy.utils.unregister_class(array.OBJECT_OT_array2d)
    bpy.utils.unregister_class(array.OBJECT_OT_array3d)
    bpy.utils.unregister_class(objects.OBJECT_OT_corncube)
    bpy.utils.unregister_class(objects.OBJECT_OT_botcube)

    bpy.types.VIEW3D_MT_mesh_add.remove(objects.menu_func)


if __package__ == "__main__":
    register()