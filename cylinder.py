import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# ===========================================
# Create Cylinder
# ===========================================

def create_cylinder(radius, height, points=50):

    vertices = []

    # Bottom circle
    theta = np.linspace(0, 2*np.pi, points, endpoint=False)

    for angle in theta:
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = 0

        vertices.append([x, y, z])

    # Top circle
    for angle in theta:
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = height

        vertices.append([x, y, z])

    vertices = np.array(vertices)

    # Faces
    faces = []

    # Curved surface
    for i in range(points):

        next_i = (i + 1) % points

        faces.append([
            i,
            next_i,
            next_i + points,
            i + points
        ])

    # Bottom face
    faces.append(list(range(points)))

    # Top face
    faces.append(list(range(points, 2*points)))

    return vertices, faces


# ===========================================
# Draw Cylinder
# ===========================================

def draw_cylinder(vertices, faces):

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    # Draw vertices
    ax.scatter(
        vertices[:,0],
        vertices[:,1],
        vertices[:,2],
        color="black",
        s=20
    )

    poly3d = []

    for face in faces:

        polygon = []

        for vertex_index in face:
            polygon.append(vertices[vertex_index])

        poly3d.append(polygon)

    cylinder = Poly3DCollection(
        poly3d,
        facecolor="cyan",
        edgecolor="black",
        linewidth=0.5,
        alpha=0.6
    )

    ax.add_collection3d(cylinder)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    xmin, ymin, zmin = vertices.min(axis=0)
    xmax, ymax, zmax = vertices.max(axis=0)

    ax.set_xlim(xmin-1, xmax+1)
    ax.set_ylim(ymin-1, ymax+1)
    ax.set_zlim(zmin-1, zmax+1)

    ax.set_box_aspect([
        xmax-xmin,
        ymax-ymin,
        zmax-zmin
    ])

    plt.show()


# ===========================================
# Main Program
# ===========================================

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

vertices, faces = create_cylinder(radius, height)

draw_cylinder(vertices, faces)