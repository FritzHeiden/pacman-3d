import os
from pacman3d.model import Model

class ModelLoader:
    def load(self, path):
        model = Model()
        model.vertices = []
        model.normals = []
        model.faces = []

        lines = open(path, "r").read().split("\n")
        for line in lines:
            if line.startswith("v "):
                vertices = line.split(" ")
                model.vertices.append((float(vertices[1]), float(vertices[2]), float(vertices[3])))
            elif line.startswith("vn "):
                normals = line.split(" ")
                model.vertices.append((float(normals[1]), float(normals[2]), float(normals[3])))
            elif line.startswith("f "):
                faces = line.split(" ")
                model.faces.append((int(faces[1].split("//")[0]), int(faces[2].split("//")[0]), int(faces[3].split("//")[0])))

        return model
