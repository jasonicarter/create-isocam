﻿# This script creates two kinds of isometric cameras.
#The one, TrueIsocam called camera, is the mathematical correct isometric camera with the 54.736 rotation to get the 30 degrees angles at the sides of the rhombus.
#The other, GameIsocam called camera, is a camera with which you can render isometric tiles for a 2d game. Here we need a 60 degrees angle instedad of the 54.736 one to get a proper stairs effect and a ratio of 2:1
# Then there is the special case with a 4:3 ratio, which is button 3. You can also make 2D games with that one. The view is more topdown though as with a 2:1 ratio of the traditional game iso view.
# The fourth button creates a simple groundplane where you can place your stuff at.

#You can of course set up everything by hand. This script is a convenient solution so that you don't have to setup it again and again.

# The script is under Apache license

bl_info = {
    "name": "Create IsoCam",
    "description": "Creates a true isometric camera or a isometric camera for game needs",
    "author": "Reiner 'Tiles' Prokein",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Toolshelf",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Create_IsoCam",
    "category": "Create"}


import bpy

# ----------------------------------------- true isometric camera
class PR_OT_createtrueisocam(bpy.types.Operator):
    """Creates a camera for mathematical correct isometric view"""
    bl_idname = "scene.create_trueisocam"
    bl_label = "TrueIsocam"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # ----------------------------Create Camera with correct position and rotation
        bpy.ops.object.camera_add(location=(30.60861, -30.60861, 30.60861)) # Create Camera. I would love to set the rotation here too. Blender not. Not that there are no tutorials around which shows that it should work ... .

        #So that's what the next two lines are good for. Setting the rotation of the camera ...

        object = bpy.context.active_object
        object.rotation_euler = (0.955324, 0, 0.785398) #Attention, these are radians. Euler angles are (54.736,0,45) Here we set the rotation for a mathematical correct isometric view. Not to mix with the Isoview for a 2D game!

        # ------------------------------Here we adjust some settings ---------------------------------
        object.data.type = 'ORTHO' # We want Iso, so set the type of the camera to orthographic
        object.data.ortho_scale = 14.123 # Let's fit the camera to a basetile in size of 10
        object.name = "TrueIsoCam" # let's rename the cam so that it cannot be confused with other cameras.
        bpy.ops.view3d.object_as_camera() # Set the current camera as the active one to look through

        return {'FINISHED'}
# ----------------------------------------- Game isometric camera
class PR_OT_creategameisocam(bpy.types.Operator):
    """Creates a camera with isometric view for game needs"""
    bl_idname = "scene.create_gameisocam"
    bl_label = "GameIsocam"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        view_layer = bpy.context.view_layer
        # ----------------------------Create Camera with correct position and rotation
        cam1 =  bpy.data.cameras.new(name="Camera Iso Test")
        # ------------------------------Here we adjust some settings ---------------------------------

        cam1.type = 'ORTHO' # We want Iso, so set the type of the camera to orthographic
        cam1.ortho_scale=14.123 # Let's fit the camera to our basetile in size of 10
        camera = bpy.data.objects.new(name="Camera Iso", object_data =cam1)
        view_layer.active_layer_collection.collection.objects.link(camera)
        camera.location = (30.60861, -30.60861, 25.00000)
        camera.rotation_euler=(1.047198, 0, 0.785398) #Attention, these are radians. Euler angles are (60,0,45) Here we set the rotation for a isometric view that is used in 2D games. Not to mix with the mathematical correct Isoview!
       
        # Create Camera. I would love to set the rotation here too. Blender not. Not that there are no tutorials around which shows that it should work ... .

        #So that's what the next two lines are good for. Setting the rotation of the camera ...

         # let's rename the cam so that it cannot be confused with other cameras.
        bpy.ops.view3d.object_as_camera() # Set the current camera as the active one to look through


        return {'FINISHED'}

# ----------------------------------------- Game isometric camera 4 to 3
# This format is not so common. But is also used here and there. It is more topdown. With a basetile of 64 to 48 pixels

class PR_OT_creategameisocam4to3(bpy.types.Operator):
    """Creates a camera with a special 4:3 iso view for game needs"""
    bl_idname = "scene.create_gameisocam4to3"
    bl_label = "GameIsocam4to3"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # ----------------------------Create Camera with correct position and rotation
        bpy.ops.object.camera_add(location=(23.42714, -23.42714, 37.4478)) # Create Camera. I would love to set the rotation here too. Blender not. Not that there are no tutorials around which shows that it should work ... .

        #So that's what the next two lines are good for. Setting the rotation of the camera ...

        object = bpy.context.active_object
        object.rotation_euler = (0.724312, 0, 0.785398)#Attention, these are radians. Euler angles are (41.5,0,45) Here we set the rotation for a isometric view that is used in 2D games. Not to mix with the mathematical correct Isoview!

        # ------------------------------Here we adjust some settings ---------------------------------
        object.data.type = 'ORTHO' # We want Iso, so set the type of the camera to orthographic
        object.data.ortho_scale = 14.123  # Let's fit the camera to our basetile in size of 10
        object.name = "GameIso4to3Cam" # let's rename the cam so that it cannot be confused with other cameras.
        bpy.ops.view3d.object_as_camera() # Set the current camera as the active one to look through


        return {'FINISHED'}

# ----------------------------------------- Create a ground plane

class PR_OT_creategroundplane(bpy.types.Operator):
    """Creates a groundplane in size of ten where you can put your things on"""
    bl_idname = "scene.create_groundplane"
    bl_label = "Groundplane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0)) # Create Camera. I would love to set the scale here too. Blender not. So let's do it in an extra step

        object = bpy.context.active_object
        object.scale = (5, 5, 0)#The plane object is created with a size of 2. Scaling it to 10 means to scale it by factor 5
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)# apply scale

        return {'FINISHED'}

#----------------------------------------- Create panel in the toolshelf -------------------------------------------------

class PR_PT_createisocampanel(bpy.types.Panel):
    bl_label = "Create IsoCam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PR Isocam"

    def draw(self, context):

        # column buttons solution. Less space than single buttons ...
        layout = self.layout
        view = context.space_data
        # Three buttons
        col = layout.column(align=True)
        col.operator("scene.create_trueisocam", text="TrueIsocam")
        col.operator("scene.create_gameisocam", text="GameIsocam")
        col.operator("scene.create_gameisocam4to3", text="GameIso4to3cam")
        col.operator("scene.create_groundplane", text="Groundplane")
# -------------------------------------------------------------------------------------------

# store keymaps here to access after registration
addon_keymaps = []

classes = (PR_OT_createtrueisocam, PR_OT_creategameisocam, PR_OT_creategameisocam4to3, PR_OT_creategroundplane, PR_PT_createisocampanel)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
