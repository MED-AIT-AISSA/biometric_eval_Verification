import os
import numpy as np
import matplotlib.pyplot as plt

from data import genuine, impostor


def run():
    os.makedirs("plots/part2", exist_ok=True)

    bins = np.arange(0, 1.01, 0.1)

    # ---------------- Figure 1: distributions with 3 thresholds ----------------
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.hist(impostor, bins=bins, alpha=0.6, color="red", label="Impostor scores")
    ax.hist(genuine, bins=bins, alpha=0.6, color="green", label="Genuine scores")

    ax.axvline(0.50, color="blue", linestyle=":", label="tau = 0.50")
    ax.axvline(0.60, color="black", linestyle="--", linewidth=2, label="tau = 0.60")
    ax.axvline(0.70, color="purple", linestyle=":", label="tau = 0.70")

    ax.set_xlabel("similarity score")
    ax.set_ylabel("number of comparisons")
    ax.set_title("Genuine and impostor score distributions")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.savefig("plots/part2/part2_distributions.png", dpi=150)
    plt.close(fig)

    # ---------------- Figure 2: where the errors are (tau = 0.60) ----------------
    tau = 0.60

    fig, ax = plt.subplots(figsize=(9, 5.5))

    # every score is one dot: genuine on the top line, impostor on the bottom line
    for s in genuine:
        if s < tau:
            ax.scatter(s, 1, color="orange", s=120, edgecolors="black")   # false non-match
        else:
            ax.scatter(s, 1, color="green", s=120, edgecolors="black")
    for s in impostor:
        if s >= tau:
            ax.scatter(s, 0, color="orange", s=120, edgecolors="black")   # false match
        else:
            ax.scatter(s, 0, color="red", s=120, edgecolors="black")

    ax.axvline(tau, color="black", linestyle="--", linewidth=2)
    ax.axvspan(0, tau, alpha=0.08, color="red")
    ax.axvspan(tau, 1, alpha=0.08, color="green")

    ax.text(0.02, 1.25, "Rejected zone (s < tau)", fontsize=11)
    ax.text(0.66, 1.25, "Accepted zone (s >= tau)", fontsize=11)
    ax.text(0.45, 1.12, "false non-matches", color="darkorange", fontsize=11)
    ax.text(0.45, -0.18, "false match (0.62)", color="darkorange", fontsize=11)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Impostor", "Genuine"])
    ax.set_ylim(-0.4, 1.5)
    ax.set_xlim(0, 1)
    ax.set_xlabel("similarity score")
    ax.set_title("Where the errors happen (tau = 0.60). Orange dots = errors")
    ax.grid(alpha=0.3)
    fig.savefig("plots/part2/part2_errors_tau060.png", dpi=150)
    plt.close(fig)

    # ---------------- Text answer ----------------
    print("=== Score distributions ===")
    print("Genuine scores go from", min(genuine), "to", max(genuine))
    print("Impostor scores go from", min(impostor), "to", max(impostor))
    print("The two ranges overlap between", min(genuine), "and", max(impostor))
    print("Overlap zone = errors: no threshold can separate the two groups perfectly.")
    print()
    print("Plots saved in: plots/part2")
