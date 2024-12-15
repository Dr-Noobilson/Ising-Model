import numpy as np
import matplotlib.pyplot as plt

def plot_map(lattice, lattice_new, b, J, iter, n, figsize):

    fig, ax = plt.subplots(1, 2, figsize=figsize)

    binary_lattice = (lattice + 1) // 2
    binary_lattice_new = (lattice_new + 1) // 2

    ax[0].imshow(binary_lattice, cmap="binary", origin="upper")
    ax[0].axis('on')  # Show axes
    # ax[0].set_title(f"Original Lattice")
    
    ax[1].imshow(binary_lattice_new, cmap="binary", origin="upper")
    ax[1].axis('on')  # Show axes
    # ax[1].set_title(f"Updated Lattice")
    
    plt.suptitle(f"[b = {b}, J = {J}, iter = {iter}, n = {n}]", fontsize=8)

    plt.tight_layout()
    plt.show()

def plot_3map(spin_matrices, spin_matrices_new, b, J, iter, n, figsize):

    for i in range(3):
        lattice = spin_matrices[i, :, :]
        lattice_new = spin_matrices_new[i, :, :]
        fig, ax = plt.subplots(1, 2, figsize=figsize)

        binary_lattice = (lattice + 1) // 2
        binary_lattice_new = (lattice_new + 1) // 2

        ax[0].imshow(binary_lattice, cmap="binary", origin="upper")
        ax[0].axis('on')  # Show axes
        # ax[0].set_title(f"Original Lattice")
        
        ax[1].imshow(binary_lattice_new, cmap="binary", origin="upper")
        ax[1].axis('on')  # Show axes
        # ax[1].set_title(f"Updated Lattice")
        
        plt.suptitle(f"[axis = {i+1}, b = {b}, J = {J}, iter = {iter}, n = {n}]", fontsize=8)

        plt.tight_layout()
        plt.show()