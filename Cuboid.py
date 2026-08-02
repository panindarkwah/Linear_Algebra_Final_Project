import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# ============================================
# Create Cuboid
# ============================================

def create_cuboid(length, width, height):

    vertices = np.array([
        [0, 0, 0],
        [length, 0, 0],
        [length, width, 0],
        [0, width, 0],
        [0, 0, height],
        [length, 0, height],
        [length, width, height],
        [0, width, height]
    ])

    faces = [
        [0,1,2,3],     # Bottom
        [4,5,6,7],     # Top
        [0,1,5,4],     # Front
        [2,3,7,6],     # Back
        [0,3,7,4],     # Left
        [1,2,6,5]      # Right
    ]

    return vertices, faces


# ============================================
# Draw Object
# ============================================

def draw_object(vertices, faces):

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    # Draw vertices
    ax.scatter(
        vertices[:,0],
        vertices[:,1],
        vertices[:,2],
        color='black',
        s=40
    )

    # Build polygons
    poly3d = []

    for face in faces:
        poly3d.append([vertices[i] for i in face])

    # Draw faces
    ax.add_collection3d(
        Poly3DCollection(
            poly3d,
            facecolors=[
                "red",
                "blue",
                "green",
                "yellow",
                "orange",
                "purple"
            ],
            edgecolors="black",
            linewidths=0.5,
            alpha=0.6
        )
    )

    # Axis labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Axis limits
    ax.set_xlim(-1,5)
    ax.set_ylim(-1,3)
    ax.set_zlim(-1,4)

    # Equal scaling
    ax.set_box_aspect([4,2,3])

    plt.show()


# ============================================
# Main Program
# ============================================

print("Creating and drawing a cuboid with dimensions 4x2x3...")
print("Enter the length of the cuboid :")
length = float(input())
print("Enter the width of the cuboid :")
width = float(input())
print("Enter the height of the cuboid :")
height = float(input())

vertices, faces = create_cuboid(length, width, height)

draw_object(vertices, faces)

print("Choose an object:")
print("1. Cube")
print("2. Cuboid")
print("3. Pyramid")
print("4. Cone")
print("5. Cylinder")

choice = input("Enter your choice: ")

