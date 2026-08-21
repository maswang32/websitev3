import os
from glob import glob

import numpy as np
from skimage.color import rgb2lab, lab2rgb
from matplotlib.colors import to_rgb, to_hex

from pyvis.network import Network


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
        descendants = self._collect_unique_descendants()
        return sum(node.base_area for node in descendants)

    def _collect_unique_descendants(self):
        descendants = set()
        stack = [self]
        while stack:
            node = stack.pop()
            descendants.add(node)
            stack.extend(node.children)
        return descendants


class KnowledgeGraph:
    def __init__(self):
        self.node_dict = {}

    def add(
        self,
        name,
        base_area=25,
        parent_names=(),
        color=None,
    ):
        self.node_dict[name] = Node(
            name=name,
            base_area=base_area,
            parents=[self.node_dict[parent] for parent in parent_names],
            color=color,
        )

    def find_note_paths(self):
        # Dict mapping node file stems to note paths.
        node_stems_to_note_paths = {}
        notes_dir = os.path.join(os.path.dirname(__file__), "notes")

        # recursive=True allows **
        markdown_paths = glob(os.path.join(notes_dir, "**", "*.md"), recursive=True)
        for path in markdown_paths:
            node_stem = os.path.splitext(os.path.basename(path))[0]
            if node_stem in node_stems_to_note_paths:
                raise ValueError(
                    f"Duplicate markdown files: {node_stem} is found in {node_stems_to_note_paths[node_stem]} and {path}"
                )
        node_stems_to_note_paths[node_stem] = path
        return node_stems_to_note_paths

    def render(self):
        pyvisnet = Network(
            bgcolor="#000000",
            font_color="white",
            width="100%",  # Fill page horizontally
            height="100vh",  # Graph is one viewport tall (browser window)
        )

        node_stems_to_note_paths = self.find_note_paths()

        for node in self.node_dict.values():
            # Compute Radius
            radius = np.sqrt(node.compute_area())

            # Look up associated notes
            hyphenated_name = node.name.replace(" ", "-")
            note_path = node_stems_to_note_paths.get(hyphenated_name)

            if not note_path:
                node_text = ""
            else:
                relative_path = os.path.relpath(note_path, os.path.dirname(__file__))
                page_url = f"https://masonlwang.com/knowledgegraph/{relative_path[:-3].replace('\\', '/')}/"
                with open(note_path, encoding="utf-8") as f:
                    node_text = f.read()

            # Define node appearance
            node_attrs = {
                "label": node.name,
                "title": node_text,
                "size": radius,
                "mass": radius**2 / 100,
            }

            if not note_path:
                node_attrs["color"] = node.color
            else:
                node_attrs["color"] = {
                    "background": node.color,
                    "border": "white",
                    "borderWidth": 1,
                }
                node_attrs["href"] = page_url
                assert node.base_area > 0, (
                    f"Node {node.name} with existing notes must have positive size"
                )

            # Add the node to the pyvisnet
            pyvisnet.add_node(node.name, **node_attrs)
