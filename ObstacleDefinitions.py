#Brendan Neal
#ENPM661
#This Script Will Initialize the Robot dimensions and all Obstacle dimensions in this Project

import numpy as np


#Robot Information
RobotRadius = 0
Clearance_Temp = 5 #mm
Clearance = RobotRadius + Clearance_Temp

##----------------------------------Original Obstacles-------------------------------##
BotRec_X_BL_Corner = 100
BotRec_Y_BL_Corner = 0

BotRec_X_BR_Corner = 150
BotRec_Y_BR_Corner = 0

BotRec_X_TL_Corner = 100
BotRec_Y_TL_Corner = 100 

BotRec_X_TR_Corner = 150 
BotRec_Y_TR_Corner = 100 

Bottom_Rectangle_Points = np.array([[BotRec_X_TL_Corner, BotRec_Y_TL_Corner],
                                    [BotRec_X_BL_Corner, BotRec_Y_BL_Corner],
                                    [BotRec_X_BR_Corner, BotRec_Y_BR_Corner],
                                    [BotRec_X_TR_Corner, BotRec_Y_TR_Corner]])

#Top Rectangle

TopRec_X_BL_Corner = 100 
TopRec_Y_BL_Corner = 150 

TopRec_X_BR_Corner = 150 
TopRec_Y_BR_Corner = 150 

TopRec_X_TL_Corner = 100 
TopRec_Y_TL_Corner = 250

TopRec_X_TR_Corner = 150 
TopRec_Y_TR_Corner = 250

Top_Rectangle_Points = np.array([[TopRec_X_TL_Corner, TopRec_Y_TL_Corner],
                                    [TopRec_X_BL_Corner, TopRec_Y_BL_Corner], 
                                    [TopRec_X_BR_Corner, TopRec_Y_BR_Corner],
                                    [TopRec_X_TR_Corner, TopRec_Y_TR_Corner]])


#Middle Hexagon
#Theory: A hexagon is made up of 6 equalateral triangles.
CenterX = 300
CenterY = 125

X_Top_Right_Corner = int(CenterX + 75*np.cos(np.deg2rad(30)))
Y_Top_Right_Corner = int(CenterY + 75*np.sin(np.deg2rad(30)))

X_Bottom_Right_Corner = int(CenterX + 75*np.cos(np.deg2rad(-30)))
Y_Bottom_Right_Corner = int(CenterY + 75*np.sin(np.deg2rad(-30)))

X_TopMost_Corner = int(CenterX )
Y_TopMost_Corner = int(CenterY + 75)

X_BottomMost_Corner = int(CenterX)
Y_BottomMost_Corner = int(CenterY - 75)

X_Top_Left_Corner = int(CenterX - 75*np.cos(np.deg2rad(30))) 
Y_Top_Left_Corner = int(CenterY + 75*np.sin(np.deg2rad(30)))

X_Bottom_Left_Corner = int(CenterX - 75*np.cos(np.deg2rad(-30)))
Y_Bottom_Left_Corner = int(CenterY + 75*np.sin(np.deg2rad(-30)))

Hexagon_Points = np.array([[X_BottomMost_Corner, Y_BottomMost_Corner],
                           [X_Bottom_Right_Corner, Y_Bottom_Right_Corner],
                           [X_Top_Right_Corner, Y_Top_Right_Corner],
                           [X_TopMost_Corner, Y_TopMost_Corner],
                           [X_Top_Left_Corner, Y_Top_Left_Corner],
                           [X_Bottom_Left_Corner, Y_Bottom_Left_Corner]
                           ], dtype=np.int32)


#Triangle
Bot_Tri_CornerX = 460 
Bot_Tri_CornerY = 25 

Top_Tri_CornerX = 460 
Top_Tri_CornerY = 225 

Right_Tri_CornerX = 510 
Right_Tri_CornerY = 125

Triangle_Points = np.array([[Bot_Tri_CornerX, Bot_Tri_CornerY],
                            [Top_Tri_CornerX, Top_Tri_CornerY],
                            [Right_Tri_CornerX, Right_Tri_CornerY]])


##-----------------------------Extended Obstacle Spaces------------------------------##

#Bottom Rectangle

BotRec_X_BL_Corner_Ext = 100 - Clearance
BotRec_Y_BL_Corner_Ext = 0

BotRec_X_BR_Corner_Ext = 150 + Clearance
BotRec_Y_BR_Corner_Ext = 0

BotRec_X_TL_Corner_Ext = 100 - Clearance
BotRec_Y_TL_Corner_Ext = 100 + Clearance

BotRec_X_TR_Corner_Ext = 150 + Clearance
BotRec_Y_TR_Corner_Ext = 100 + Clearance

Bottom_Rectangle_Points_OBS = np.array([[BotRec_X_TL_Corner_Ext, BotRec_Y_TL_Corner_Ext],
                                    [BotRec_X_BL_Corner_Ext, BotRec_Y_BL_Corner_Ext],
                                    [BotRec_X_BR_Corner_Ext, BotRec_Y_BR_Corner_Ext],
                                    [BotRec_X_TR_Corner_Ext, BotRec_Y_TR_Corner_Ext]])

#Top Rectangle

TopRec_X_BL_Corner_Ext = 100 - Clearance
TopRec_Y_BL_Corner_Ext = 150 - Clearance

TopRec_X_BR_Corner_Ext = 150 + Clearance
TopRec_Y_BR_Corner_Ext = 150 - Clearance

TopRec_X_TL_Corner_Ext = 100 - Clearance
TopRec_Y_TL_Corner_Ext = 250

TopRec_X_TR_Corner_Ext = 150 + Clearance
TopRec_Y_TR_Corner_Ext = 250

Top_Rectangle_Points_OBS = np.array([[TopRec_X_TL_Corner_Ext, TopRec_Y_TL_Corner_Ext],
                                    [TopRec_X_BL_Corner_Ext, TopRec_Y_BL_Corner_Ext], 
                                    [TopRec_X_BR_Corner_Ext, TopRec_Y_BR_Corner_Ext],
                                    [TopRec_X_TR_Corner_Ext, TopRec_Y_TR_Corner_Ext]])


#Middle Hexagon
#Theory: A hexagon is made up of 6 equalateral triangles.
CenterX = 300
CenterY = 125

X_Top_Right_Corner_Ext = int(CenterX + 75*np.cos(np.deg2rad(30)) + Clearance)
Y_Top_Right_Corner_Ext = int(CenterY + 75*np.sin(np.deg2rad(30)))

X_Bottom_Right_Corner_Ext = int(CenterX + 75*np.cos(np.deg2rad(-30)) + Clearance)
Y_Bottom_Right_Corner_Ext = int(CenterY + 75*np.sin(np.deg2rad(-30)))

X_TopMost_Corner_Ext = int(CenterX )
Y_TopMost_Corner_Ext = int(CenterY + 75 + Clearance)

X_BottomMost_Corner_Ext = int(CenterX )
Y_BottomMost_Corner_Ext = int(CenterY - 75 - Clearance)

X_Top_Left_Corner_Ext = int(CenterX - 75*np.cos(np.deg2rad(30)) - Clearance)
Y_Top_Left_Corner_Ext = int(CenterY + 75*np.sin(np.deg2rad(30)))

X_Bottom_Left_Corner_Ext = int(CenterX - 75*np.cos(np.deg2rad(-30)) - Clearance)
Y_Bottom_Left_Corner_Ext = int(CenterY + 75*np.sin(np.deg2rad(-30)))

Hexagon_Points_OBS = np.array([[X_BottomMost_Corner_Ext, Y_BottomMost_Corner_Ext],
                           [X_Bottom_Right_Corner_Ext, Y_Bottom_Right_Corner_Ext],
                           [X_Top_Right_Corner_Ext, Y_Top_Right_Corner_Ext],
                           [X_TopMost_Corner_Ext, Y_TopMost_Corner_Ext],
                           [X_Top_Left_Corner_Ext, Y_Top_Left_Corner_Ext],
             
                           [X_Bottom_Left_Corner_Ext, Y_Bottom_Left_Corner_Ext]
                           ], dtype=np.int32)


#Triangle
Bot_Tri_CornerX_Ext = 460 - Clearance
Bot_Tri_CornerY_Ext = 25 - 3*Clearance #Needed to Tack on Extra to get the proper side extension.

Top_Tri_CornerX_Ext = 460 - Clearance
Top_Tri_CornerY_Ext = 225 + 3*Clearance #Needed to Tack on Extra to get the proper side extension.

Right_Tri_CornerX_Ext= 510 + 2*Clearance #Needed to Tack on Extra to get the proper side extension.
Right_Tri_CornerY_Ext = 125

Triangle_Points_OBS = np.array([[Bot_Tri_CornerX_Ext, Bot_Tri_CornerY_Ext],
                            [Top_Tri_CornerX_Ext, Top_Tri_CornerY_Ext],
                            [Right_Tri_CornerX_Ext, Right_Tri_CornerY_Ext]])

