import numpy as np

class CubicToOrthorhombic():
    """
    Define a crystal structure.
    """
    def __init__(self, lattice_constant, martensite_a, martensite_b, martensite_c):
        """
        Store a parent lattice constant and martensite lattice constant
        CV1 : T1, CV2 : T2, CV3 : T3, CV4 : T4, CV5 : T5, CV6 : T6
        """
        self.lattice_constant = lattice_constant
        self.martensite_a = martensite_a
        self.martensite_b = martensite_b
        self.martensite_c = martensite_c
        self.alpha = martensite_a / lattice_constant
        self.beta = martensite_b / np.sqrt(2) / lattice_constant
        self.gamma = martensite_c / np.sqrt(2) / lattice_constant
        self.T1 = np.array([[self.alpha,0,0],[0,(self.beta + self.gamma)/2, (self.beta - self.gamma)/2],[0, (self.beta - self.gamma)/2, (self.beta + self.gamma)/2]])
        self.T2 = np.array([[self.alpha,0,0],[0,(self.beta + self.gamma)/2, (-self.beta + self.gamma)/2],[0, (-self.beta + self.gamma)/2, (self.beta + self.gamma)/2]])
        self.T3 = np.array([[(self.beta + self.gamma)/2, 0, (self.beta - self.gamma)/2], [0, self.alpha, 0],[(self.beta - self.gamma)/2, 0, (self.beta + self.gamma)/2]])
        self.T4 = np.array([[(self.beta + self.gamma)/2, 0, (-self.beta + self.gamma)/2], [0, self.alpha, 0],[(-self.beta + self.gamma)/2, 0, (self.beta + self.gamma)/2]])
        self.T5 = np.array([[(self.beta + self.gamma)/2, (self.beta - self.gamma)/2, 0],[(self.beta - self.gamma)/2, (self.beta + self.gamma)/2, 0],[0, 0, self.alpha]])
        self.T6 = np.array([[(self.beta + self.gamma)/2, (-self.beta + self.gamma)/2, 0],[(-self.beta + self.gamma)/2, (self.beta + self.gamma)/2, 0],[0, 0, self.alpha]])
        
    def show_lattice_constant(self):
        print(lattice_constant)
        
    def show_lattice_distortion_matrix(self):
        print("T1 = \n", self.T1)
        print("T2 = \n", self.T2)
        print("T3 = \n", self.T3)
        print("T4 = \n", self.T4)
        print("T5 = \n", self.T5)
        print("T6 = \n", self.T6)
        
    def arbitary_orientation_CV_strain(self, transformation_matrix="T1", orientation = np.array([1, 1, 1])):
        """
        orientation strain based on transformation matrix and orientation
        """
        if transformation_matrix == "T1":
            transformation_matrix_used = self.T1
        elif transformation_matrix == "T2":
            transformation_matrix_used = self.T2
        
        x_dash = np.dot(self.T1, orientation)
        epsilon = (np.linalg.norm(x_dash) - np.linalg.norm(orientation)) / np.linalg.norm(orientation)
        
        print(epsilon)
        
    def fixed_orientation_arbitary_CV_strain(self, orientation = np.array([1, 1, 1])):
        """
        Choose an orientation that you want to use and output all strains of CVs.
        """
        x_dash = [np.dot(self.T1, orientation), np.dot(self.T2, orientation), np.dot(self.T3, orientation), 
                  np.dot(self.T4, orientation), np.dot(self.T5, orientation), np.dot(self.T6, orientation)]

        epsilon = []        
        i = 0
        for i in range(6):
            epsilon += [(np.linalg.norm(x_dash[i]) - np.linalg.norm(orientation)) / np.linalg.norm(orientation)]
        
        print("CV1 : \n", epsilon[0])
        print("CV2 : \n", epsilon[1])
        print("CV3 : \n", epsilon[2])
        print("CV4 : \n", epsilon[3])
        print("CV5 : \n", epsilon[4])
        print("CV6 : \n", epsilon[5])
        
    def compression_strain(self, orientation = np.array([1, 1, 1])):
        """
        Return a minimum transformation strain subjected to the orientation.
        """
        x_dash = [np.dot(self.T1, orientation), np.dot(self.T2, orientation), np.dot(self.T3, orientation), 
                  np.dot(self.T4, orientation), np.dot(self.T5, orientation), np.dot(self.T6, orientation)]

        epsilon = []        
        i = 0
        for i in range(6):
            epsilon += [(np.linalg.norm(x_dash[i]) - np.linalg.norm(orientation)) / np.linalg.norm(orientation)]
        
        minimum_epsilon = min(epsilon)

        return -1 * minimum_epsilon
    
    def tensile_strain(self, orientation = np.array([1, 1, 1])):
        """
        Return a maximum transformation strain subjected to the orientation.
        """
        x_dash = [np.dot(self.T1, orientation), np.dot(self.T2, orientation), np.dot(self.T3, orientation), 
                  np.dot(self.T4, orientation), np.dot(self.T5, orientation), np.dot(self.T6, orientation)]

        epsilon = []        
        i = 0
        for i in range(6):
            epsilon += [(np.linalg.norm(x_dash[i]) - np.linalg.norm(orientation)) / np.linalg.norm(orientation)]
        
        return max(epsilon)
        