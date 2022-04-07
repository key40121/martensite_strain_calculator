import math

import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.axes_grid1 import make_axes_locatable

def imshow_xy_coordinate(point = np.array([1, 1, 1]), figsize=(15, 12), hide_axis=False):
    """
    Create a xy coordinates system including a single mirror index.
    """

    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(1, 1, 1)
    xy = mirror_index_to_xy(mirror_index = point)
    ax.scatter(xy[0], xy[1])

    ax.set_aspect('equal')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

def imshow_xy_coordinates(x_coordinate, y_coordinate, figsize=(15, 12),
                             hide_axis=False, plot_label=False):
    """
    Create a xy coordinates system including mirror indices.
    """

        
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(1, 1, 1)
        
    ax.scatter(x_coordinate, y_coordinate)
        
    if plot_label:
        """
        This algorithm is so bad. 
        """
        annotations = all_indices[1:]
        temp_list = []
            
        for i in range(1, len(annotations)):
                
            if not([math.floor(1000*x_coordinate[i]), math.floor(1000*y_coordinate[i])] in temp_list):
                    
                ax.annotate(annotations[i], (x_coordinate[i], y_coordinate[i]))
                temp_list.append([math.floor(1000*x_coordinate[i]), math.floor(1000*y_coordinate[i])])
        
    ax.set_aspect('equal')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
        
def imshow_contour(mirror_index_list, coordinate, figsize=(15, 12), 
                   xlim=(0,1), ylim=(0,1), marker=False, 
                   cmap=plt.cm.jet, hide_axis=False, plot_label=False):
    """
    Create a xy coordinate system and a contour map on it.
    """

    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(1, 1, 1)

# Drawing a contour
    ax.tricontour(x,y,z,
                   20,             
                   linewidths=0.3, 
                   linestyles='dotted',
                   colors='black'
                  )

# Painting between each line 
    cntr = ax.tricontourf(x,y,z,
                           20,             
                           cmap=cmap  
                          )
    # Drawing a colorbar
    fig.colorbar(cntr, ax=ax)


    
    if marker:
        ax.plot(x, y, "ko", ms=3) # marker='ko' (kuro, circle), markersize=3
        
        if plot_label: # Plot mirror indices with marker dots.
        # Remember mirror_index_list has [0 0 0] at the first element of the list

            annotations = mirror_index_list[1:]
            temp_list = []
            
            for i in range(1, len(annotations)):
                
                if not([math.floor(100*x[i]), math.floor(100*y[i])] in temp_list):
                    
                    ax.annotate(annotations[i], (x[i], y[i]))
                    temp_list.append([math.floor(100*x[i]), math.floor(100*y[i])])
        
        
    ax.axis((-2,2,-2,2))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    
    if hide_axis:
        ax.axis("off")

    plt.show()
    
def imshow_contour_triangle(coordinate, figsize=(15, 12),  
                            xlim=(0,0.42), ylim=(0,0.42), cmap="jet", 
                            contour_number=20, line_style="solid", line_width=1.5,
                            hide_axis=False,  plot_label=False, cbar_vertical=True):
    """
    Create a standard stereographic triangle contour based on the selected experimental mode. 
    """

    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(1, 1, 1)

# Drawing a contour
    ax.tricontour(x,y,z, 
                  contour_number,             
                   linewidths=line_width, 
                   linestyles=line_style,
                   colors='black'
                  )

# Painting between each line 
    cntr = ax.tricontourf(x,y,z,
                            contour_number,             
                           cmap=cmap  # RdBu_r=(Red,Blue), PuBu_r=(Purple,Blue)
                          )

    
# Creating colorbar and fix the size of it based on the actual size of the triangle 
    divider = make_axes_locatable(ax)
    

    if cbar_vertical:
        cax = divider.append_axes("right", size="5%", pad=0.5)
        fig.colorbar(cntr, ax=ax, cax=cax)
    else:
        cax = divider.append_axes("bottom", size="5%", pad=0.5)
        fig.colorbar(cntr, ax=ax, cax=cax, orientation="horizontal")


    if plot_label: # Plot mirror indices with marker dots.
        
        # Remember mirror_index_list has [0 0 0] at the first element of the list
        annotations = [[0, 0, 1], [1, 0, 1], [1, 1, 1]]
        x = [0, 0.414213562373094, 0.366025403784438]
        y = [0, 0, 0.366025403784438]
            
        for i in range(len(annotations)):
            ax.plot(x, y, "ko", ms=3)
            ax.annotate(annotations[i], (x[i], y[i]))
        
    ax.axis((-2,2,-2,2))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    
    if hide_axis:
        ax.axis("off")

    plt.show()
    


