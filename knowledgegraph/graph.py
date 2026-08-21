import numpy as np
from skimage.color import rgb2lab, lab2rgb
from matplotlib.colors import to_rgb, to_hex


class Node:
    def __init__(
        self,
        name,
        base_area,
        parents,
        color,
    ):
        self.name = name
        self.base_area = base_area
        self.parents = parents

        if color is None:
            if len(parents) > 0:
                self.color = self.interpolate_parent_colors()
            else:
                raise ValueError("Must specify node color if node has no parents")
        else:
            self.color = color

    def interpolate_parent_colors(self):
        node_colors_rgb = [to_rgb(node.color) for node in self.parents]
        node_colors_lab = rgb2lab(node_colors_rgb)
        avg_color_lab = np.mean(node_colors_lab, axis=0)
        avg_color_rgb = lab2rgb(avg_color_lab)
        return to_hex(avg_color_rgb)
