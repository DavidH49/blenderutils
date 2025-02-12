# SPDX-FileCopyrightText: 2025 DDD
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


def select_mesh(obj):
    obj.select_set(True)
    obj.matrix_world = bpy.context.scene.cursor.matrix


def deselect_all():
    for o in bpy.context.selected_objects:
        o.select_set(False)


def recalc_normals():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()


def construct_cube(position=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.translate(value=position)
    bpy.ops.object.editmode_toggle()