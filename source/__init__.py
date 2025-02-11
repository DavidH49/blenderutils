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
    "version": (2, 0, 0),
    "location": "",
    "warning": "",
    "category": "Generic",
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(misc)
    importlib.reload(array)
    importlib.reload(objects)
    importlib.reload(util)
else:
    from . import ui
    from . import util
    from .ops import misc
    from .ops import array
    from .ops import objects

import bpy


CLASSES = (
    ui.VIEW3D_PT_ddd_utils,
    ui.VIEW3D_PT_ddd_array,
    misc.OBJECT_OT_quickbevel,
    misc.OBJECT_OT_quickmirror,
    array.OBJECT_OT_array1d,
    array.OBJECT_OT_array2d,
    array.OBJECT_OT_array3d,
    objects.OBJECT_OT_corncube,
    objects.OBJECT_OT_botcube
)


def register():
    for c in CLASSES:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_mesh_add.append(objects.menu_func)


def unregister():
    for c in reversed(CLASSES):
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_mesh_add.remove(objects.menu_func)


if __package__ == "__main__":
    register()