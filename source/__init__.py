# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

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


from .ops import misc
from .ops import array
from .ops import objects
from . import util
from . import ui

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

    bpy.types.VIEW3D_MT_mesh_add.append(ui.objects_menu)


def unregister():
    for c in reversed(CLASSES):
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_mesh_add.remove(ui.objects_menu)


if __package__ == "__main__":
    register()