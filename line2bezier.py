#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Convert straight line to Bezier curve. Input straight line need to be in a projected coordinate system.
# Created by LIU,Zheng. March 1 2017.
#

import os, arcpy  
from math import atan2, pi
import arcpy.cartography as CA

#
# Add vertext to line
#
in_fc = arcpy.GetParameterAsText(0)
  
def shiftPointInDirection(firstx, firsty, lastx, lasty, length):  
	degrees = (atan2(lasty - firsty, lastx - firstx)) * 180.0 / pi  
	if degrees < 0:  
		degrees = 360 + degrees  
	if  0<=degrees<90:
		x1,y1 = lastx - length*0.3, lasty - length*0.07
	elif 90<=degrees<180:		
		x1,y1 = lastx + length*0.3, lasty - length*0.07
	elif 180<=degrees<270:
		x1,y1 = lastx + length*0.3, lasty + length*0.07
	elif 270<=degrees<=360:
		x1,y1 = lastx - length*0.3, lasty + length*0.07
	return (x1, y1)  
  
# create a inmemo polyline feature class and add field(s)  
addVertex = arcpy.CreateFeatureclass_management("in_memory", "addVertex", "POLYLINE", spatial_reference = arcpy.Describe(in_fc).spatialReference).getOutput(0)  
arcpy.AddField_management(addVertex, "ORIGID", "LONG")  
  
# starting an edit session may not be necessary, but to stay on the safe side...  
workspace = os.path.dirname(in_fc)  
with arcpy.da.Editor(workspace) as edit:  
  
	with arcpy.da.SearchCursor(in_fc, ["SHAPE@", "OID@"]) as sc:  
	 with arcpy.da.InsertCursor(addVertex, ["SHAPE@", "ORIGID"]) as ic:  
	  for row in sc:  
		shp = row[0]
		length = shp.getLength("PLANAR","METERS")
		firstPoint = shp.firstPoint  
		lastPoint = shp.lastPoint  
# handle individual vertices  
		p0 = firstPoint  
		p2 = lastPoint  
		x1,y1 = shiftPointInDirection(p0.X, p0.Y, p2.X, p2.Y, length)  
		p1 = arcpy.Point(x1, y1)  
# create new feature and store it  
		new_geometry = arcpy.Polyline(arcpy.Array([p0, p1, p2]))  
		new_row = [new_geometry, row[1]]  
		ic.insertRow(new_row)  

#
# Convert to Bezier curve
#
smoothedFeatures = arcpy.GetParameterAsText(1)
CA.SmoothLine(addVertex, smoothedFeatures, "BEZIER_INTERPOLATION", "", "", "NO_CHECK")
# Delete inmemo fc
arcpy.Delete_management("in_memory")