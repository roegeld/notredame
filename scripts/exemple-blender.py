import bpy
from mathutils import Matrix
# quelque chose comme cela doit permettre
# de charger plusieurs objets dans Blender
# et de les translater convenablement

# les valeurs de location proviennent du fichier positions.txt

# Pour lancer ce script, lancez Blender, puis ouvrez Text Editor,
# chargez le script et faites Run Script.

BA1=bpy.ops.import_scene.obj(filepath='BA1.obj')
bpy.data.objects["BA1"].select=True
tmatrix=Matrix.Translation((0, 0, 0))
bpy.data.objects["BA1"].data.transform(tmatrix)

BA2=bpy.ops.import_scene.obj(filepath='BA2.obj')
bpy.data.objects["BA2"].select=True
tmatrix=Matrix.Translation((0.0,700.0,0.0))
bpy.data.objects["BA2"].data.transform(tmatrix)

BB1=bpy.ops.import_scene.obj(filepath='BB1.obj')
bpy.data.objects["BB1"].select=True
tmatrix=Matrix.Translation((-1065.4,350.0,104.0))
bpy.data.objects["BB1"].data.transform(tmatrix)

BB2=bpy.ops.import_scene.obj(filepath='BB2.obj')
bpy.data.objects["BB2"].select=True
tmatrix=Matrix.Translation((-225.0,350.0,104.0))
bpy.data.objects["BB2"].data.transform(tmatrix)

BB3=bpy.ops.import_scene.obj(filepath='BB3.obj')
bpy.data.objects["BB3"].select=True
tmatrix=Matrix.Translation((225.0,350.0,104.0))
bpy.data.objects["BB3"].data.transform(tmatrix)

BB4=bpy.ops.import_scene.obj(filepath='BB4.obj')
bpy.data.objects["BB4"].select=True
tmatrix=Matrix.Translation((1065.4,350.0,104.0))
bpy.data.objects["BB4"].data.transform(tmatrix)

