import matplotlib.pyplot as plt #Import Matplotlib module
import numpy as np #import Numpy module




Plot_Size = int(input("what size would you want your graph to be ? : ")) #Asking for the X and Y max values
if Plot_Size < 0:
    raise NameError("Come on mate, positives values ONLY")

plt.axis([0, Plot_Size, 0, Plot_Size]) #Defining plot size

print('\n')

How_M_Points = int(input("How many random starting points would you like to generate ? (min 3) : ")) #Asking for the number of random starting point to generate
if How_M_Points < 3:
    raise NameError("Values below 3 are not accepted")

print('\n')

Divisor = int(input("What number would you like to divide by ? (The minimum default is 2) : ")) #Asking for the number they want to divise the distance by
if Divisor < 2:
    raise NameError("Values below 2 are not accepted")

print('\n')

NB_Iteration = int(input("How many iteration would you like to do ? (the biggest value the best, but try to keep it reasonnable :D) : ")) #Asking for the number of iterations
if NB_Iteration < 1:
    raise NameError("The value is too small")

print('\n')

print("For the next questions if you wish to choose random points, just hit [ENTER]", end = '\n')

print('\n')

Rand_UStartPointX = input("Choose the X coordonates for your starting point : ") #Asking for the User to choose the X coordonates of their starting point
if Rand_UStartPointX == "":
    Rand_UStartPointX = np.random.randint(0, Plot_Size, 1)
elif not(int(Rand_UStartPointX)):
    raise NameError("The value is not an int")
elif int(Rand_UStartPointX) < 0 or int(Rand_UStartPointX) > Plot_Size:
    raise NameError("The value is not contain within the range of plot size you chose")

print('\n')

Rand_UStartPointY = input("Choose the Y coordonates for your starting point : ") #Asking for the User to choose the Y coordonates of their starting point
if Rand_UStartPointY == "":
    Rand_UStartPointY = np.random.randint(0, Plot_Size, 1)
elif not(int(Rand_UStartPointY)):
    raise NameError("The value is not an int")
elif int(Rand_UStartPointY) < 0 or int(Rand_UStartPointY) > Plot_Size:
    raise NameError("The value is not contain within the range of plot size you chose")


Rand_UStartPointX = int(Rand_UStartPointX) #Just converting the str to int to avoid any problem when calculating
Rand_UStartPointY = int(Rand_UStartPointY)

print('\n')

print("Bip Boop,  Generating the plot, biiip boopiipp")



StartPoint_XList = np.random.randint(0, Plot_Size, How_M_Points) #Generating list of X coordonates for starting points and assign them random values


StartPoint_YList = np.random.randint(0, Plot_Size, How_M_Points) #Generating list of Y coordonates for starting points and assign them random values



def Middle_Xcoordonates(x1, x2): #Calculate the middle X coordonates between x1 and x2
    x3 = (x1+x2)/Divisor
    return x3

def Middle_Ycoordonates(y1, y2): #Calculate the middle Y coordonates between y1 and y2
    y3 = (y1+y2)/Divisor
    return y3


List_AllDrawingPoints = [[Rand_UStartPointX, Rand_UStartPointY]]

plt.scatter(StartPoint_XList, StartPoint_YList, s=30, edgecolors='none', c='red', label = 'Random Starting Points') #Draw all the starting points
plt.scatter(Rand_UStartPointX, Rand_UStartPointY, s=25, edgecolors='black', c='red', label = 'User Starting Point') #Draw User's starting point

for i in range(NB_Iteration):

    point = np.random.randint(0, How_M_Points, 1) #Toss a "How_M_Points" sided dice

    midx = Middle_Xcoordonates(List_AllDrawingPoints[i-1][0], StartPoint_XList[point]) #Calculate the middle point between the current point and one of the starting point (chosen by the dice)
    midy = Middle_Ycoordonates(List_AllDrawingPoints[i-1][1], StartPoint_YList[point]) #Same as above but for Y

    plt.scatter(midx, midy, s=10, edgecolors='none', c='green') #Place the points on the graph
    List_AllDrawingPoints.append((midx, midy)) #Append the new middle point to the list of all points


#Just doing this to be able to put one label and not NB_Iteration numbers label
#Yes it's dirty but it works

point = np.random.randint(0, How_M_Points, 1) #Toss a "How_M_Points" sided dice

midx = Middle_Xcoordonates(List_AllDrawingPoints[i-1][0], StartPoint_XList[point]) #Calculate the middle point between the current point and one of the starting point (chosen by the dice)
midy = Middle_Ycoordonates(List_AllDrawingPoints[i-1][1], StartPoint_YList[point]) #Same as above but for Y

plt.scatter(midx, midy, s=10, edgecolors='none', c='green', label = "Points Calculated") #Place the points on the graph

plt.legend() #Show Legend
plt.show() #Show the plot
