# Cameron Kerr: May 9 2023 #
# Convex hull calculator using Graham Scan algorithm #

import random
import math as m
import matplotlib.pyplot as plt

def all_index(lst:list, value: int) -> list:
    '''
    Returns a list of the indices of value in lst
    '''
    indices = [i for i, j in enumerate(lst) if j == value]
    return indices


def sort_by_angles(x:list, y:list, px:int, py:int):
    '''
    Returns x and y sorted according to their angles in respect to px and py. 
    If more than 1 x,y coordinates have the same angle, only keep the farthest 
    from px, py
    '''
    # For each point which is not the starting point, calculate polar angle with
    # respect to the x-axis and the starting point
    angles = []
    distances = []
    for i in range(len(x)):
        if x[i] != px:
            angle =  m.atan2((y[i] - py),(x[i] - px))
        elif y[i] != py:
            angle = m.pi/2
        else:
            angle = None
        angles.append(angle)  
        d = m.sqrt((x[i]-px)**2 + (y[i] - py)**2)   
        distances.append(d)
    p_index = angles.index(None)
    angles.pop(p_index)
    distances.pop(p_index)
    x.pop(p_index)
    y.pop(p_index)

    # Sort all parallel lists according to increasing angles
    x_sorted = [x for _, x in sorted(zip(angles, x))]
    y_sorted = [y for _, y in sorted(zip(angles, y))]
    d_sorted = [distances for _, distances in sorted(zip(angles, distances))]
    a_sorted = sorted(angles)
    
    # Make all angles unique by only keeping point of farthest distance out of 
    # a set of points with the same angle
    new_x = []
    new_y = []
    for angle in sorted(list(set(a_sorted))):
        indices = all_index(a_sorted, angle)
        d_of_angle = [d_sorted[i] for i in indices]
        index = indices[d_of_angle.index(max(d_of_angle))]
        #index = [indices for _, indices in sorted(zip(d_of_angle, indices))][-1]
        new_x.append(x_sorted[index])
        new_y.append(y_sorted[index])
    return new_x, new_y


def plot_convex_hull(x,y, testing = False):
    '''
    Plots the outline of the convex hull of set of points given by x, y
    '''
    convex_hull_x = []
    convex_hull_y = []
    
    # Find starting point
    if y.count(min(y)) == 1:
        convex_hull_y.append(min(y))
        x_min_y = x[y.index(min(y))]
        convex_hull_x.append(x_min_y)
    else:
        x_min_y = [x[i] for i in all_index(y, min(y))]
        min_x_min_y = min(x_min_y)
        convex_hull_y.append(min(y))
        convex_hull_x.append(min_x_min_y)
    
    x, y = sort_by_angles(x,y,convex_hull_x[0], convex_hull_y[0])
        
    # Add in another point
    convex_hull_x.append(x[0])
    convex_hull_y.append(y[0])
    
    # Loop over all points and apply Graham Scan algorithm
    x = x[1:]
    y = y[1:]
    for i in range(len(x)):
        # While the points do not move counter-clockwise, remove the middle point
        while ((convex_hull_x[-1] - convex_hull_x[-2]) * (y[i] - convex_hull_y[-2]) 
               - (convex_hull_y[-1] - convex_hull_y[-2])*(x[i] - convex_hull_x[-2]) <= 0):
            convex_hull_x.pop()
            convex_hull_y.pop()
        convex_hull_x.append(x[i])
        convex_hull_y.append(y[i])
    # Plot exterior points as line segments and plot individual interior points
    if testing == False:
        plt.plot(convex_hull_x + [convex_hull_x[0]],convex_hull_y + [convex_hull_y[0]], 'ro-')
        plt.plot(x,y, 'ro')
    
def full_function(n, testing = False):
    '''
    Generates convex hull of n randomly generated points
    '''
    x = []
    y = []
    for _ in range(n):
        y.append(random.randint(0, 1001))
        x.append(random.randint(0, 1001))
    plot_convex_hull(x,y, testing)
    
if __name__ == '__main__':
    
    # Generate convex hull for n randomly generated points
    n = input("How many points would you like to generate?")
    full_function(int(n))
    plt.show()