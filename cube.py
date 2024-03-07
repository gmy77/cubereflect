"Cube Reflection Test 1"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Cube:
    def __init__(self, center, size):
        self.center = center
        self.size = size

    def vertices(self):
        """Calcola i vertici del cubo basati sul centro e sulla dimensione."""
        d = self.size / 2
        cx, cy, cz = self.center
        return [
            (cx - d, cy - d, cz - d), (cx + d, cy - d, cz - d),
            (cx + d, cy + d, cz - d), (cx - d, cy + d, cz - d),
            (cx - d, cy - d, cz + d), (cx + d, cy - d, cz + d),
            (cx + d, cy + d, cz + d), (cx - d, cy + d, cz + d),
        ]

    def get_reflections(self, room_size):
        """Calcola le riflessioni del cubo sugli assi x, y, z."""
        reflections = []
        for axis in range(3):
            reflected = list(self.center)
            reflected[axis] = room_size[axis] - reflected[axis]
            reflections.append(Cube(tuple(reflected), self.size))
        return reflections

def plot_cube(ax, cube, color='blue', alpha=0.5):
    """Disegna un cubo su un asse Matplotlib."""
    verts = cube.vertices()
    # Lista dei lati del cubo
    faces = [[verts[j] for j in [0, 1, 2, 3]], [verts[j] for j in [4, 5, 6, 7]], 
             [verts[j] for j in [0, 3, 7, 4]], [verts[j] for j in [1, 2, 6, 5]], 
             [verts[j] for j in [0, 1, 5, 4]], [verts[j] for j in [2, 3, 7, 6]]]
    poly3d = [Poly3DCollection(faces, color=color, linewidths=1, alpha=alpha)]
    for poly in poly3d:
        ax.add_collection3d(poly)

# Inizializzazione della figura e degli assi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Definizione della stanza e dei cubi
room_size = (50, 50, 50)
cube1 = Cube((25, 25, 5), 4)
cube2 = Cube((25, 25, 13), 4)

# Plot dei cubi
plot_cube(ax, cube1, color='blue')
plot_cube(ax, cube2, color='red')

# Plot delle riflessioni
for cube_reflection in cube1.get_reflections(room_size):
    plot_cube(ax, cube_reflection, color='blue', alpha=0.2)

for cube_reflection in cube2.get_reflections(room_size):
    plot_cube(ax, cube_reflection, color='red', alpha=0.2)

# Impostazione dei limiti degli assi
ax.set_xlim(0, room_size[0])
ax.set_ylim(0, room_size[1])
ax.set_zlim(0, room_size[2])

plt.show()
