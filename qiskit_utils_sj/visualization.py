import numpy as np
import matplotlib.pyplot as plt

def plot_bloch_vector(vector):
    """Plot a single-qubit state on Bloch sphere (simplified 2D version)."""
    x, y, z = vector
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.2)

    # Draw vector
    ax.quiver(0, 0, 0, x, y, z, color='r', linewidth=2)
    ax.set_box_aspect([1,1,1])
    plt.show()

