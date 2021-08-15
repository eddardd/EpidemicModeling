import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from models import SIRModel


# For figure aesthetics
plt.rcParams['mathtext.fontset'] = 'custom'  
plt.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'  
plt.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'  
plt.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'  
plt.rcParams['font.size'] = 16
plt.rcParams['mathtext.fontset'] = 'stix'  
plt.rcParams['font.family'] = 'STIXGeneral' 

# Animation params
fp_out = "./Figures/anim_β_sir.gif"

# Colormap
cmap = matplotlib.cm.get_cmap('Reds')
color_range = matplotlib.colors.Normalize(vmin=0.04, vmax=0.4)

# Infection rate
βs = np.linspace(0.08, 0.8, 11)

# Recovery rate
γ = 0.04

# Population size
N = 1.0

time_span = np.linspace(0, 150, 300)
initial_conditions = np.array([0.99, 0.01, 0.0])
solutions = []
plt.figure()
for i in range(len(βs)):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.patch.set_facecolor((239 / 255, 239 / 255, 239 / 255))
    for ax in axes:
        ax.set_facecolor((239 / 255, 239 / 255, 239 / 255))

    for β in βs[:i]:
        # Simulation
        model = SIRModel(β, γ, N)
        solution = model(time_span, initial_conditions)
        axes[0].plot(time_span, solution[:, 0], c="#00447cff", label="$S(t)$", alpha=0.3)
        axes[1].plot(time_span, solution[:, 1], c="#800a00ff", label="$I(t)$", alpha=0.3)
        axes[2].plot(time_span, solution[:, 2], c="#008000ff", label="$R(t)$", alpha=0.3)
    β = βs[i]
    # Reproduction rate
    R0 = β / γ
    model = SIRModel(β, γ, N)
    solution = model(time_span, initial_conditions)
    axes[0].plot(time_span, solution[:, 0], c="#00447cff", label="$S(t)$")
    axes[1].plot(time_span, solution[:, 1], c="#800a00ff", label="$I(t)$")
    axes[2].plot(time_span, solution[:, 2], c="#008000ff", label="$R(t)$")
    axes[0].set_ylabel('Fração da População')
    for ax in axes:
        ax.set_xlabel('Tempo (dias)')
        ax.set_ylim([-0.05, 1.1])
        ax.text(0.0, 1.05, '$\\beta = {}$'.format(np.round(β, 3)))
    #plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig('./Figures/sir_β_{}.png'.format(11 - i))

img, *imgs = [Image.open(f) for f in ['./Figures/sir_β_{}.png'.format(i) for i in range(1, 12)]]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)