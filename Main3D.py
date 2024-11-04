import matplotlib.pyplot as plt
import numpy as np


def Distribute(NumberWalkers, X_lim, Y_lim):
    # This function is used to randomly place molecules in a plane
    # NumberWalker is the number of walkers we want to be in the plane
    # X and Y lim correspond to dimenssion of the plane 
    X_Position = np.random.randint(-X_lim, X_lim, size=NumberWalkers)
    Y_Position = np.random.randint(-Y_lim, Y_lim, size=NumberWalkers)
    Position = {}

    for i in range(1, NumberWalkers+1):
        Position[i] = [X_Position[i-1], Y_Position[i-1]]

    # Position is a dictionary whose keys are name of the walkers
        #and values correspond to position of the walkers
    return Position


#def Sticky_condition(WalkerInfo):
    # WalkerInfo is a dictionary created by Distribute, update, or even Sticky_condition function
    #for element in WalkerInfo:


def X_Y_Positions(WalkerPosition):
    #WalkerPosition is given from values of a Distribute (or Update) function
    Walker_X_Position = []
    Walker_Y_Position = []
    for element in WalkerPosition:
        Walker_X_Position.append(element[0])
        Walker_Y_Position.append(element[1])

    return [Walker_X_Position, Walker_Y_Position]


def X_Y_Z_Positions(WalkerPosition, z):
    #WalkerPosition is given from values of a Distribute (or Update) function
    Walker_X_Position = []
    Walker_Y_Position = []
    
    for element in WalkerPosition:
        Walker_X_Position.append(element[0])
        Walker_Y_Position.append(element[1])

    Walker_Z_Position = [z for i in range(len(Walker_X_Position))]

    return [Walker_X_Position, Walker_Y_Position, Walker_Z_Position]




def update(Position, Nabat_Molecules, NumberOfWalkers, X_lim, Y_lim):
    # This function updates position of the walkers after each shot
    # Nabat_Molecule_Position is a dictionary with names (keys) and positions (values) of stationary molecules
    # First we need to check which ones need to be freezed

########################################## Freezing Molecules########################################################
    Nabat_Position = X_Y_Positions(list(Nabat_Molecules.values()))
    Nabat_X_Position = Nabat_Position[0]
    Nabat_Y_Position = Nabat_Position[1]

    NamesOfWalkers = list(Position.keys())

    for name in NamesOfWalkers:
        Walker_X_Position = Position[name][0]
        Walker_Y_Position = Position[name][1]

        for i in range(len(Nabat_Position[0])):
            XelementNabat = Nabat_X_Position[i]
            YelementNabat = Nabat_Y_Position[i]
               
            if Walker_X_Position == XelementNabat + 1 or Walker_X_Position == XelementNabat - 1 :
                if Walker_Y_Position == YelementNabat:
                    Nabat_Molecules[NumberOfWalkers + 1 - len(Position)] = [Walker_X_Position, Walker_Y_Position]
                    Position.pop(name) 
                    break
                    
            elif Walker_X_Position == XelementNabat:
                if Walker_Y_Position == YelementNabat or Walker_Y_Position == YelementNabat + 1 or Walker_Y_Position == YelementNabat -1 :
                    Nabat_Molecules[NumberOfWalkers + 1 - len(Position)] = [Walker_X_Position, Walker_Y_Position]
                    Position.pop(name)  
                    break  

            elif Walker_Y_Position == YelementNabat + 1 or Walker_Y_Position == YelementNabat - 1 :
                if Walker_X_Position == XelementNabat:
                    Nabat_Molecules[NumberOfWalkers + 1 - len(Position)] = [Walker_X_Position, Walker_Y_Position]
                    Position.pop(name)   
                    break 

            elif  Walker_Y_Position == YelementNabat:
                if Walker_X_Position == XelementNabat or Walker_X_Position == XelementNabat - 1 or Walker_X_Position == XelementNabat + 1:
                    Nabat_Molecules[NumberOfWalkers + 1 - len(Position)] = [Walker_X_Position, Walker_Y_Position]
                    Position.pop(name) 
                    break   
########################################## End of Freezing Molecules ########################################################


    for Walker in Position.keys():
        DecisionNumber = np.random.rand()
        if DecisionNumber < 0.25:
            # Goes one step to right
            NewPosition = Position[Walker]

            # This condition is to make sure the molecules bounces off the boundaries
            if NewPosition[0] == X_lim:
                NewPosition[0] -= 1
            else:
                NewPosition[0] += 1
            Position.update({Walker:NewPosition})

        elif 0.25 <= DecisionNumber < 0.50:
            # Goes one step up
            NewPosition = Position[Walker]
            
            # This condition is to make sure the molecules bounces off the boundaries
            if NewPosition[1] == Y_lim:
                NewPosition[1] -= 1
            else:
                NewPosition[1] += 1
            Position.update({Walker:NewPosition})

        elif 0.5 <= DecisionNumber < 0.75:
            # Goes one step to left
            NewPosition = Position[Walker]
            
            # This condition is to make sure the molecules bounces off the boundaries
            if NewPosition[0] == -X_lim:
                NewPosition[0] += 1
            else:
                NewPosition[0] -= 1
            Position.update({Walker:NewPosition})
        else:
            # Goes one step Down
            NewPosition = Position[Walker]
            
            # This condition is to make sure the molecules bounces off the boundaries
            if NewPosition[1] == -Y_lim:
                NewPosition[1] += 1
            else:
                NewPosition[1] -= 1

            Position.update({Walker:NewPosition})
        
    
    
    return Position

def Plot(X_Position, Y_Position, Nabat_Molecules,  X_Lim, Y_Lim):
    # Nabat_Mol is a dictionary whose values give you position of the molecules which have collided
    # and won't be moving anymore
    # Plotting Walkers
    fig, ax = plt.subplots()

    ax.scatter(X_Position, Y_Position)
    # Coloring the stationary Molecules (around the string)
    xyNabaMol = X_Y_Positions(list(Nabat_Molecules.values()))
    ax.scatter(xyNabaMol[0], xyNabaMol[1], color = "yellow")
    
    # Data on the plot
    ax.set_title("Positions")
    ax.set(xlim=[-X_Lim-1, X_Lim+1], ylim=[-Y_Lim-1, Y_Lim+1]
           , xlabel='X (m)', ylabel='Y (m)')
    
    plt.xticks(np.arange(-X_Lim, X_Lim, 1))
    plt.yticks(np.arange(-Y_Lim, Y_Lim, 1))
    plt.grid(True)
    plt.show()


def main():

    iteration = 80
    # Data for 3D plot
    Data = []

    Nabat_Molecules = {}
    Nabat_Molecules[0] = [0, 0]
    

    #Dimension of the plane
    X_Limit = 25
    Y_Limit = 25
    Z_Limit = 40

    Z_Positions = [j for j in range(Z_Limit)]
    for z in Z_Positions:
        NumberOfWalkers = int(np.floor(900 * np.exp(-z/30)))
        print(NumberOfWalkers)
        # This line creates a few number of Walkers in the plane
        WalkerInfo = Distribute(NumberOfWalkers, X_Limit, Y_Limit)

        
        for counter in range(iteration):
            WalkerInfo = update(WalkerInfo, Nabat_Molecules, NumberOfWalkers, X_Limit, Y_Limit)

        
        #Plot(xyPositions[0], xyPositions[1], Nabat_Molecules, X_Limit, Y_Limit)
        
        
        Data.append(X_Y_Z_Positions(list(Nabat_Molecules.values()), z))
        WalkerInfo.clear()
        Nabat_Molecules.clear()
        Nabat_Molecules[0] = [0, 0]
    
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(Z_Limit):
        ax.scatter(Data[i][0], Data[i][1], Data[i][2])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.set(xlim=[-X_Limit-1, X_Limit+1],
           ylim=[-Y_Limit-1, Y_Limit+1],
           zlim=[0, X_Limit+1])

    plt.show()
    
    
main()
