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

        # Resolve node color
        if color is None:
            if len(parents) > 0:
                self.color = self._interpolate_parent_colors()
            else:
                raise ValueError("Must specify node color if node has no parents")
        else:
            self.color = color

        # Initialize list of children
        self.children = []

        # Add self to children of parents
        for parent in self.parents:
            parent.add_child(self)

    def _interpolate_parent_colors(self):
        node_colors_rgb = [to_rgb(node.color) for node in self.parents]
        node_colors_lab = rgb2lab(node_colors_rgb)
        avg_color_lab = np.mean(node_colors_lab, axis=0)
        avg_color_rgb = lab2rgb(avg_color_lab)
        return to_hex(avg_color_rgb)

    def add_child(self, child):
        self.children.append(child)

    def compute_area(self):
        # Note, this function also returns self
        descendant_nodes = self._collect_unique_descendant_nodes()
        return sum(node.base_area for node in descendant_nodes)

    def _collect_unique_descendant_nodes(self):
        descendant_nodes = set()
        stack = [self]
        while stack:
            node = stack.pop()
            descendant_nodes.add(node)
            stack.extend(node.children)
        return descendant_nodes
