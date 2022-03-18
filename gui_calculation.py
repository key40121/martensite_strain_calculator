from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qtmodern.styles
import qtmodern.windows
  
import sys

from crystal import CubicToOrthorhombic
from mirror_indices import MirrorIndex
import figures as fig
import dataprepare as dp
    
class Window(QWidget):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Calculator for martensitic transformation strain")
        
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
        # method for widgets
    def UiComponents(self):

        # Martensitic transformation mode
        self.widget_crystal = QComboBox(self)
        self.widget_crystal.addItems(['Cubic - Orthorhombic', 'Cubic - Orthorhombic'])
 
        # Experiment mode (tensile or compress)
        self.widget_experiment_mode = QComboBox(self)
        self.widget_experiment_mode.addItems(["Tensile", "Compress"])

        # Lattice Constants
        lattice_constant_a = QLabel("a")
        lattice_constant_b = QLabel("b")
        lattice_constant_c = QLabel("c")
        lattice_constant_a0 = QLabel("a0")

        self.widget_a = QLineEdit(self)
        self.widget_a.setText("0.3126")
        self.widget_b = QLineEdit(self)
        self.widget_b.setText("0.4870")
        self.widget_c = QLineEdit(self)
        self.widget_c.setText("0.4646")
        self.widget_aa = QLineEdit(self)
        self.widget_aa.setText("0.3285")

        # Mirror index
        widget_label_mirror_index = QLabel("mirror index")
        self.widget_mirror_index = QComboBox(self)
        self.widget_mirror_index.addItems([str(i) for i in range(3, 21)])
        

        # ColorBar
        self.widget_label_contour = QLabel("The number of level")
        self.widget_contour = QComboBox(self)
        self.widget_contour.addItems([str(i) for i in range(10, 51)])
        self.widget_color_bar = QComboBox(self)
        self.widget_color_bar.addItems(["jet", "hsv", "CMRmap", "GnBu", "RdBu", 
                                                    "Spectral", "afmhot", "coolwarm", "gnuplot",
                                                    "terrain" ])
        self.widget_color_bar_2 = QComboBox(self)
        self.widget_color_bar_2.addItems(["Vertical", "Horizontal"])

        # x-y limits
        # Hide axis

        # Start calculation and create a figure
        widget_button = QPushButton("Create a figure", self)
        widget_button.clicked.connect(self.start_calculation)

        # Horizontal layout
        # mode
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.widget_crystal)
        hbox_1.addWidget(self.widget_experiment_mode)
        hbox_1.addWidget(widget_label_mirror_index)
        hbox_1.addWidget(self.widget_mirror_index)

        # Lattice constant
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(lattice_constant_a)
        hbox_2.addWidget(self.widget_a)
        hbox_2.addWidget(lattice_constant_b)
        hbox_2.addWidget(self.widget_b)
        hbox_2.addWidget(lattice_constant_c)
        hbox_2.addWidget(self.widget_c)
        hbox_2.addWidget(lattice_constant_a0)
        hbox_2.addWidget(self.widget_aa)

        # color bar
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.widget_label_contour)
        hbox_3.addWidget(self.widget_label_contour)
        hbox_3.addWidget(self.widget_contour)
        hbox_3.addWidget(self.widget_color_bar)
        hbox_3.addWidget(self.widget_color_bar_2)

        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(widget_button)

        # vertical layout
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)


        self.setLayout(vbox)
    
    def start_calculation(self):

        # show a  
        print(self.widget_crystal.currentText())
        print(self.widget_experiment_mode.currentText())
        print(self.widget_mirror_index.currentText())
        print(self.widget_contour.currentText())
        print(self.widget_color_bar.currentText())
        print(self.widget_color_bar_2.currentText())

        parent_lattice_constant = float(self.widget_aa.text())
        martensite_lattice_constant_a = float(self.widget_a.text())
        martensite_lattice_constant_b = float(self.widget_b.text())
        martensite_lattice_constant_c = float(self.widget_c.text())

        mirror_index_used = int(self.widget_mirror_index.currentText())
        contour_number = int(self.widget_contour.currentText())
        cmap = self.widget_color_bar.currentText()
        
        # Implementation
        crystal = CubicToOrthorhombic(parent_lattice_constant, 
                                                    martensite_lattice_constant_a, martensite_lattice_constant_b, 
                                                    martensite_lattice_constant_c)
        mirror_index = MirrorIndex(mirror_index_used)

        if self.widget_experiment_mode.currentText() == "Tensile":
            transformation_mode = crystal.tensile_strain
        else:
            transformation_mode = crystal.compression_strain

        xyz = dp.coordinate_contour_triangle(mirror_index.mirror_indices_list(), transformation_mode)
        fig.imshow_contour_triangle(xyz, xlim=(0, 0.42), ylim=(0, 0.42), cmap=cmap, 
                    contour_number=contour_number, plot_label=False, hide_axis=True)


def main():
    # create pyqt5 app
    app = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()

    # Using third party's thema
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    # start the app
    app.exec_()

if __name__=='__main__':
    main()