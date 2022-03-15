# glTF-Blender-IO-MSFS
# Copyright (C) 2020-2021 The glTF-Blender-IO-MSFS authors

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bpy
from .msfs_light import MSFSLight
from .msfs_gizmo import MSFSGizmo
from .msfs_material import MSFSMaterial
from .msfs_material_animation import MSFSMaterialAnimation

class Import:

    def __init__(self):
        pass

    # Create lights
    def gather_import_light_after_hook(self, gltf2_node, blender_node, blender_light, import_settings):
        MSFSLight.create(gltf2_node, blender_node, blender_light, import_settings)

    # Create gizmos
    def gather_import_node_after_hook(self, vnode, gltf2_node, blender_object, import_settings):
        MSFSGizmo.create(gltf2_node, blender_object, import_settings)

    # Create materials
    def gather_import_material_after_hook(self, gltf2_material, vertex_color, blender_material, import_settings):
        MSFSMaterial.create(gltf2_material, blender_material, import_settings)

    # Create material animations
    def gather_import_scene_after_nodes_hook(self, gltf2_scene, blender_scene, import_settings): # TODO: move this to proper animation hook once added
        MSFSMaterialAnimation.create(import_settings)
