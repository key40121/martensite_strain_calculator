import itertools

import numpy as np
import sympy

class MirrorIndex():
    """
    Define a mirror indices on the xy coordinates.
    """
    def __init__(self, number):
        """
        Define a number that would be used to define an indices list.
        For example, if a number is 1, 
        then create the list including [000], [001], [010],..,[111] 
        """
        self.number = number
        self.mirror_indices_list()
    
    def mirror_indices_list(self):
            """
            Return a numpy array that has all possible indices 
            """
            candidate = []
            for i in range(self.number + 1):
                candidate += [i]
        
            all_combinations = itertools.product(candidate, repeat = 3)
        
            list_temp = []
            for x in all_combinations:
                list_temp.append(x)
            
            all_indices = np.array(list_temp)
        
            return all_indices
    
    def xy_coordinates(self):
        """
        Create (x, y) coordinates based on mirror indices.
        """
        x_coordinate = []
        y_coordinate = []
        
        for i in range(1, len(self.all_indices)):
            
            norm_index = np.linalg.norm(self.all_indices[i])
            mirror_index_on_sphere = self.all_indices[i] / norm_index
            
            OQ = np.array([0, 0, -1])
            QR = mirror_index_on_sphere - OQ
            
            sympy.var('t')
            parameter = sympy.solve(OQ[2] + t * QR[2], t)
            x = OQ[0] + QR[0] * parameter[0]
            y = OQ[1] + QR[1] * parameter[0]
            
            x_coordinate.append(x)
            y_coordinate.append(y)

        return x_coordinate, y_coordinate

def main():
    temp = MirrorIndex(3)
    print(temp.mirror_indices_list())

if __name__=='__main__':
    main()