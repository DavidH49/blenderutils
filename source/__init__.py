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
    "version": (1, 4, 0),
    "location": "",
    "warning": "",
    "category": "Generic",
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(ops_misc)
    importlib.reload(ops_array)
    importlib.reload(ops_objects)
    importlib.reload(util)
else:
    from . import ui
    from . import ops_misc
    from . import ops_array
    from . import ops_objects
    from . import util

import bpy


def register():
    bpy.utils.register_class(ui.VIEW3D_PT_ddd_utils)
    bpy.utils.register_class(ui.VIEW3D_PT_ddd_array)
    bpy.utils.register_class(ops_misc.OBJECT_OT_quickbevel)
    bpy.utils.register_class(ops_misc.OBJECT_OT_quickmirror)
    bpy.utils.register_class(ops_array.OBJECT_OT_array1d)
    bpy.utils.register_class(ops_array.OBJECT_OT_array2d)
    bpy.utils.register_class(ops_array.OBJECT_OT_array3d)
    bpy.utils.register_class(ops_objects.OBJECT_OT_corncube)
    bpy.utils.register_class(ops_objects.OBJECT_OT_botcube)

    bpy.types.VIEW3D_MT_mesh_add.append(ops_objects.menu_func)


def unregister():
    bpy.utils.unregister_class(ui.VIEW3D_PT_ddd_utils)
    bpy.utils.unregister_class(ui.VIEW3D_PT_ddd_array)
    bpy.utils.unregister_class(ops_misc.OBJECT_OT_quickbevel)
    bpy.utils.unregister_class(ops_misc.OBJECT_OT_quickmirror)
    bpy.utils.unregister_class(ops_array.OBJECT_OT_array1d)
    bpy.utils.unregister_class(ops_array.OBJECT_OT_array2d)
    bpy.utils.unregister_class(ops_array.OBJECT_OT_array3d)
    bpy.utils.unregister_class(ops_objects.OBJECT_OT_corncube)
    bpy.utils.unregister_class(ops_objects.OBJECT_OT_botcube)

    bpy.types.VIEW3D_MT_mesh_add.remove(ops_objects.menu_func)


if __package__ == "__main__":
    register()