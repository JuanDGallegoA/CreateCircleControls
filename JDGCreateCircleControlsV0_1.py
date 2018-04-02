# JDG CreateCircleControls V0.1
# Create circle controls for each item selected
# Script Made by Juan David Gallego Arango :)
# Animacion101@gmail.com

import maya.cmds as cmds
    
def autoControls (node):
	cmds.circle(radius=1, ch=False, n=(node +'ctrl'))
	cmds.select(node+ 'ctrl' + 'Shape')
	cmds.select(node, add=True)
	cmds.parent(r=True, s=True)
	cmds.delete(node +'ctrl')
	print 'control aplicado a ' + node
	
for item in cmds.ls(selection=True):
	autoControls(item)
	
# Working
