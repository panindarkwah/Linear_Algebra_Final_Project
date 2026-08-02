import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def create_cone(radius, height, points=100):

    vertices = []

    # -------------------------
    # Apex
    # -------------------------
    vertices.append([0, 0, height])

    # -------------------------
    # Base circle
    # -------------------------
    theta = np.linspace(0, 2*np.pi, points, endpoint=False)

    for angle in theta:

        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = 0

        vertices.append([x, y, z])

    vertices = np.array(vertices)

    # -------------------------
    # Faces
    # -------------------------

    faces = []

    # Side triangles
    for i in range(1, points + 1):

        next_i = i + 1

        if next_i > points:
            next_i = 1

        faces.append([
            0,
            i,
            next_i
        ])

    # Base face
    faces.append(list(range(1, points + 1)))

    return vertices, faces

def draw_cone(vertices, faces):

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection="3d")

    # Draw vertices
    ax.scatter(
        vertices[:,0],
        vertices[:,1],
        vertices[:,2],
        color="black",
        s=15
    )

    poly3d = []

    for face in faces:

        polygon = []

        for index in face:

            polygon.append(vertices[index])

        poly3d.append(polygon)

    cone = Poly3DCollection(
        poly3d,
        facecolor="cyan",
        edgecolor="black",
        linewidth=0.5,
        alpha=0.6
    )

    ax.add_collection3d(cone)

    # Labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Automatic limits
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
    
    
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

vertices, faces = create_cone(radius, height)

draw_cone(vertices, faces)