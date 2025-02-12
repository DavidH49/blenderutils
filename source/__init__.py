# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

from .ops import modifiers
from .ops import add_obj
from .ops import edit_obj
from . import util
from . import ui

import bpy


CLASSES = (
    ui.VIEW3D_PT_ddd_utils,
    ui.VIEW3D_PT_ddd_array,
    modifiers.OBJECT_OT_quickbevel,
    modifiers.OBJECT_OT_quickmirror,
    modifiers.OBJECT_OT_array1d,
    modifiers.OBJECT_OT_array2d,
    modifiers.OBJECT_OT_array3d,
    edit_obj.OBJECT_OT_resetobj,
    add_obj.OBJECT_OT_corncube,
    add_obj.OBJECT_OT_botcube
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