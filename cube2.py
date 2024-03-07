"Cube Reflection Test 2"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

class Cube:
    def __init__(self, center, size):
        self.center = np.array(center)
        self.size = size

    def get_vertices(self):
        half_size = self.size / 2
        # Vertici del cubo rispetto al centro
        vertices = [
            self.center + np.array([half_size, half_size, half_size]),
            self.center + np.array([-half_size, half_size, half_size]),
            self.center + np.array([-half_size, -half_size, half_size]),
            self.center + np.array([half_size, -half_size, half_size]),
            self.center + np.array([half_size, half_size, -half_size]),
            self.center + np.array([-half_size, half_size, -half_size]),
            self.center + np.array([-half_size, -half_size, -half_size]),
            self.center + np.array([half_size, -half_size, -half_size])
        ]
        return vertices

    def get_reflection(self, axis, room_size):
        # Riflette il cubo lungo un dato asse
        reflection = Cube(self.center, self.size)
        reflection.center[axis] = room_size[axis] - self.center[axis]
        return reflection

def plot_cube(vertices, ax, color='blue'):
    # Crea le facce del cubo dalla lista dei vertici
    edges = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]], 
        [vertices[0], vertices[1], vertices[5], vertices[4]], 
        [vertices[2], vertices[3], vertices[7], vertices[6]], 
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[4], vertices[7], vertices[3], vertices[0]]
    ]
    ax.add_collection3d(Poly3DCollection(edges, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))

# Parametri della stanza e dei cubi
room_size = np.array([50, 50, 50])
cube1 = Cube((25, 25, 5), 4)
cube2 = Cube((25, 25, 13), 4)

# Creazione della figura e dell'asse
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definizione dei limiti degli assi
ax.set_xlim(0, room_size[0])
ax.set_ylim(0, room_size[1])
ax.set_zlim(0, room_size[2])

# Plot dei cubi originali
plot_cube(cube1.get_vertices(), ax, 'blue')
plot_cube(cube2.get_vertices(), ax, 'green')

# Plot delle riflessioni dei cubi
for axis in range(3):
    reflected_cube1 = cube1.get_reflection(axis, room_size)
    reflected_cube2 = cube2.get_reflection(axis, room_size)
    plot_cube(reflected_cube1.get_vertices(), ax, 'lightblue')
    plot_cube(reflected_cube2.get_vertices(), ax, 'lightgreen')

plt.show()
