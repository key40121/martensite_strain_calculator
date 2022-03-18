import numpy as np
import sympy
import math

def coordinate_contour(mirror_index_list, crystal_strain):
    """
    Return (x, y, z) coordinate based on mirror indices list and crystal strain
    """
    x_coordinate = []
    y_coordinate = []
    z_coordinate = []
    
    
    
    for i in range(1, len(mirror_index_list)):
        x_coordinate.append(mirror_index_to_xy(mirror_index_list[i])[0])
        y_coordinate.append(mirror_index_to_xy(mirror_index_list[i])[1])
        
    for i in range(1, len(mirror_index_list)):
        z_coordinate.append(crystal_strain(mirror_index_list[i]) * 100)
        
    return x_coordinate, y_coordinate, z_coordinate

def mirror_index_to_xy(mirror_index = np.array([1, 1, 1])):
    """
    mirror index to x, y coordinates in the reverse pole figure
    """
    absolute_index = np.linalg.norm(mirror_index)
    mirror_index_along_sphere = mirror_index / absolute_index
    
    # p = OQ + t*QR
    OQ = np.array([0, 0, -1])
    QR = mirror_index_along_sphere - OQ

    sympy.var('t')
    parameter = sympy.solve(OQ[2] + t*QR[2], t)

    x = OQ[0] + QR[0] * parameter[0]
    y = OQ[1] + QR[1] * parameter[0]
    
    return [x, y]

def coordinate_contour_triangle(mirror_index_list, crystal_strain):
    """
    Return (x, y, z) coordinate based on mirror indices list and crystal strain
    """
    x_coordinate = []
    y_coordinate = []
    z_coordinate = []
    
    
    for i in range(1, len(mirror_index_list)):
        
        x_adding = mirror_index_to_xy(mirror_index_list[i])[0]
        y_adding = mirror_index_to_xy(mirror_index_list[i])[1]
        z_adding = crystal_strain(mirror_index_list[i]) * 100
        

    
        A = np.array([-0.414213562373094, 0, 0], dtype=float)
        O = np.array([0, 0, -1], dtype=float)
    
        B = np.array([x_adding, y_adding, 0], dtype=float)
        OA = A - O
        OB = B - O
        OB_abs = np.linalg.norm(OB)
        OA_abs = np.linalg.norm(OA)
        inner = np.dot(OA, OB)
        
        cos_theta = inner / (OB_abs * OA_abs)
        theta_1 = math.degrees(math.acos(cos_theta))
        
        if x_adding == 0:
            x_temp = 0.001
            tan_theta = y_adding / x_temp
            theta_2 = math.degrees(math.atan(tan_theta))
        else:
            tan_theta = y_adding / x_adding
            theta_2 = math.degrees(math.atan(tan_theta))
        
        if theta_1 < 46 and theta_2 < 46:
            x_coordinate.append(x_adding)
            y_coordinate.append(y_adding)
            z_coordinate.append(z_adding)
        
    return x_coordinate, y_coordinate, z_coordinate