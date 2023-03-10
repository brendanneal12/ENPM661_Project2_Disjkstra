#Brendan Neal
#ENPM661 Project 2
#Directory ID: bneal12

##---------Importing Functions-----------##
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
import timeit
import queue
from queue import PriorityQueue

##----Importing Variables from Other Files-----##
from ObstacleDefinitions import *

##-------Generating Node Class-----------##
class Node():
    #Initializing Function
    def __init__(self, state, parent, move, C2C):
        self.state = state
        self.parent = parent
        self.move = move
        self.C2C = C2C
    #Methods for this Class
    def ReturnState(self):
        return self.state
    
    def ReturnMove(self):
        return self.move
    
    def ReturnParent(self):
        return self.parent
    
    def ReturnParentState(self):
        if self.ReturnParent() is None:
            return None

        return self.ReturnParent().ReturnState()
    
    def ReturnCost(self):
        return self.C2C
    
    def __lt__(self, other):
        return self.C2C < other.C2C
    
    def ReturnPath(self):
        moves = []
        nodes = []
        CurrentNode = self
        while(CurrentNode.ReturnMove() is not None):
            moves.append(CurrentNode.ReturnMove())
            nodes.append(CurrentNode)
            CurrentNode = CurrentNode.ReturnParent()
        nodes.append(CurrentNode)
        nodes.reverse()
        moves.reverse()

        return moves, nodes
    

##------------------Defining my Check in Workspace? Function-------##    
def CheckInWorkspace(CurrentX, CurrentY):
    WsX_Extended = 600-1
    WsY_Extended = 250-1
    if (CurrentX > WsX_Extended or int(CurrentX)<1 or int(CurrentY)<1 or CurrentY>WsY_Extended):
        return 1
    return 0
    
##-------------------Defining my Check in Obstacles? Function-------##

def CheckInObstacles(CurrentX, CurrentY, Rectangle1OS, Rectangle2OS, TriangleOS, HexOS):
    Rec1Check = cv.pointPolygonTest(Rectangle1OS, (CurrentX, CurrentY), False)
    Rec2Check = cv.pointPolygonTest(Rectangle2OS, (CurrentX, CurrentY), False)
    TriCheck = cv.pointPolygonTest(TriangleOS, (CurrentX, CurrentY), False)
    HexCheck = cv.pointPolygonTest(HexOS, (CurrentX, CurrentY), False)
    if Rec1Check > 0:
        return 1
    if Rec2Check > 0:
        return 1
    if TriCheck > 0:
        return 1
    if HexCheck > 0:
        return 1
    else:
        return 0
    
##---------------Defining my Action Set within one Function----------##
''' This function generates the possible moves and checks whether the move is valid by checking if the move leads into
 an obstacle, out of the workspace, or the move takes you to the previous parent all in one go.'''
def GeneratePossibleMoves(CurrentNode):
    x, y = CurrentNode.ReturnState()
    moves = ['Up','UpRight', 'Right', 'DownRight', 'Down', 'DownLeft','Left', 'UpLeft']
    possible_moves = ['Up','UpRight', 'Right', 'DownRight', 'Down', 'DownLeft','Left', 'UpLeft']
    move_x = [x, x+1, x+1, x+1, x, x-1, x-1, x-1]
    move_y = [y+1, y+1, y, y-1, y-1, y-1, y, y+1]
    for move in range(len(moves)):
        if (CheckInObstacles(move_x[move], move_y[move],Bottom_Rectangle_Points_OBS ,Top_Rectangle_Points_OBS, Triangle_Points_OBS, Hexagon_Points_OBS) or CheckInWorkspace(move_x[move], move_y[move]) or CurrentNode.ReturnParentState() == [move_x[move], move_y[move]]):
            possible_moves.remove(moves[move])
    return possible_moves

#Defining my Map Coloring Function
def WSColoring(Workspace, Location, Color):
    x,y,_ = Workspace.shape
    translation_y = Location[0]
    translation_x = x - Location[1] - 1
    Workspace[translation_x,translation_y,:] = Color
    return Workspace

##--------------Defining my GetInitialState Function-------------##
def GetInitialState():
    print("Enter initial node, separated by spaces: ")
    Init_State=[int(x) for x in input().split()]
    return Init_State


##--------------Defining my GetGoalState Function-------------##
def GetGoalState():
    print("Enter goal node, separated by spaces: ")
    Goal_State=[int(x) for x in input().split()]
    return  Goal_State

#----------------Defining my Compare to Goal Function------------------##

def CheckGoal(CurrentNode, GoalNode):
    if np.array_equal(CurrentNode, GoalNode) or CurrentNode == GoalNode:
        return True
    else:
        return False

##-----------------------"Main Script"---------------------------##

#Area Information
SizeAreaX = 600
SizeAreaY = 250

Workspace = np.zeros((SizeAreaY, SizeAreaX,3))
Workspace[:,:] = (0,0,0)

#Drawing Extended Obstacle Space Using Half Panes
Rectangle1_Obs_Space = cv.fillPoly(Workspace, [Bottom_Rectangle_Points_OBS], [255,0,0])
Rectangle2_Obs_Space = cv.fillPoly(Workspace, [Top_Rectangle_Points_OBS], [255,0,0])
Triangle_Obs_Space = cv.fillPoly(Workspace, [Triangle_Points_OBS], [255,0,0])
Hexagon_Obs_Space = cv.fillPoly(Workspace, [Hexagon_Points_OBS], [255,0,0])

#Drawing Original Obstacles
Rectangle1= cv.fillPoly(Workspace, [Bottom_Rectangle_Points], [0,0,255])
Rectangle2 = cv.fillPoly(Workspace, [Top_Rectangle_Points], [0,0,255])
Triangle= cv.fillPoly(Workspace, [Triangle_Points], [0,0,255])
Hexagon = cv.fillPoly(Workspace, [Hexagon_Points], [0, 0, 255])

plt.imshow(Workspace, origin='lower')
plt.show()

InitState = GetInitialState()
GoalState = GetGoalState()

if CheckInObstacles(InitState[0], InitState[1], Bottom_Rectangle_Points_OBS , Top_Rectangle_Points_OBS, Triangle_Points_OBS, Hexagon_Points_OBS):
    print("Initial State is in an obstacle, please restart")
    exit()

if CheckInObstacles(GoalState[0], GoalState[1], Bottom_Rectangle_Points_OBS , Top_Rectangle_Points_OBS, Triangle_Points_OBS, Hexagon_Points_OBS):
    print("Goal State is in an obstacle, please restart")
    exit()

if CheckInWorkspace(InitState[0], InitState[1]):
    print("Initial State is Outside of Workspace, please restart")
    exit()

if CheckInWorkspace(GoalState[0], GoalState[1]):
    print("Goal State is Outside of Workspace, please restart")
    exit()

Open_List = PriorityQueue()
starting_node = Node(InitState, None, None, 0)
Open_List.put((starting_node.ReturnCost(), starting_node))
GoalReach = False

Moves_C2C = {'Up':1 ,'UpRight':1.4, 'Right':1, 'DownRight':1.4, 'Down':1, 'DownLeft':1.4,'Left':1, 'UpLeft':1.4}
Closed_List = np.array([[Node([i,j],None, None, math.inf)for j in range(SizeAreaY)]for i in range(SizeAreaX)])

Working_Space = WSColoring(Workspace, InitState, [0,255,0])
Working_Space = WSColoring(Workspace, GoalState, [0,255,0])
plt.imshow(Working_Space)
plt.show()

##CONDUCT DIJKSTRA

starttime = timeit.default_timer()
print("Dijkstra Search Starting!!!!")

while not (Open_List.empty() and GoalReach):
    current_node = Open_List.get()[1]
    i, j = current_node.ReturnState()
    Working_Space = WSColoring(Working_Space, current_node.ReturnState(), [255, 255, 255])

    XMoves = {'Up':i ,'UpRight':i+1, 'Right':i+1, 'DownRight':i+1, 'Down':i, 'DownLeft':i-1,'Left':i-1, 'UpLeft':i-1}
    YMoves = {'Up':j+1 ,'UpRight':j+1, 'Right':j, 'DownRight':j-1, 'Down':j-1, 'DownLeft':j-1,'Left':j, 'UpLeft':j+1}
    Moves_C2C = {'Up':1 ,'UpRight':1.4, 'Right':1, 'DownRight':1.4, 'Down':1, 'DownLeft':1.4,'Left':1, 'UpLeft':1.4}

    goalreachcheck = CheckGoal(current_node.ReturnState(), GoalState)

    if goalreachcheck:
        print("Goal Reached!")
        print("Total Cost:", current_node.ReturnCost())
        MovesPath, Path = current_node.ReturnPath()

        for nodes in Path:
            Position = nodes.ReturnState()
            Working_Space = WSColoring(Working_Space, Position, [255,0,255])

    else:
        NewNode = GeneratePossibleMoves(current_node)
        Parent_Cost = current_node.ReturnCost()

        for move in NewNode:
            Child_Position = [XMoves.get(move), YMoves.get(move)]
            print("Possible Moves Are:", Child_Position)
            C2C = Parent_Cost + Moves_C2C.get(move)

            if(Closed_List[Child_Position[0], Child_Position[1]].ReturnCost() == math.inf):
               New_Child = Node(Child_Position, current_node, move, C2C)
               Closed_List[Child_Position[0], Child_Position[1]] = New_Child

               Open_List.put((New_Child.ReturnCost(), New_Child))


            else:
                if(C2C < Closed_List[Child_Position[0], Child_Position[1]].ReturnCost()):
                    New_Child = Node(Child_Position, current_node, move, C2C)
                    Closed_List[Child_Position[0], Child_Position[1]] = New_Child
                    Open_List.put((New_Child.ReturnCost(), New_Child))

    if goalreachcheck:
        break

stoptime = timeit.default_timer()

print("The Algorithm took", stoptime-starttime, "seconds to solve.")

plt.imshow(Working_Space)
plt.show()



