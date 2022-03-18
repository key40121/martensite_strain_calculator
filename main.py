from crystal import CubicToOrthorhombic
from mirror_indices import MirrorIndex
import figures as fig
import dataprepare as dp

def main():
    # Crystal instance.
    crystal = CubicToOrthorhombic(0.3285, 0.3126, 0.4870, 0.4646)
    # Mirror index instance.
    mirror_index = MirrorIndex(3)
    # Define (x, y, z) coordinates for a contour figure.
    xyz = dp.coordinate_contour_triangle(mirror_index.mirror_indices_list(), crystal.compression_strain)
    # Create a contour figure based on coordinates that is defined above.
    fig.imshow_contour_triangle(xyz, xlim=(0, 0.42), ylim=(0, 0.42), contour_number=20, plot_label=True, hide_axis=True)

if __name__=='__main__':
    main()

