import os
import numpy as np
import matplotlib.pyplot as plt

from data import genuine, impostor, FTA, rates


def run():
    os.makedirs("plots/part1", exist_ok=True)

    thresholds = [0.50, 0.60, 0.70]

    # ---------------- Questions 1, 2, 3 ----------------
    all_results = []

    for tau in thresholds:
        print()
        print("=== Threshold tau =", tau, "===")

        # which genuine comparisons are rejected?
        rejected = []
        for s in genuine:
            if s < tau:
                rejected.append(s)

        # which impostor comparisons are accepted?
        accepted = []
        for s in impostor:
            if s >= tau:
                accepted.append(s)

        print("Genuine scores rejected (false non-matches):", rejected)
        print("Impostor scores accepted (false matches)   :", accepted)

        FMR, FNMR, TAR, TRR, FAR, FRR = rates(tau)

        print("--- Matcher level ---")
        print("FMR  =", round(FMR, 3))
        print("FNMR =", round(FNMR, 3))
        print("TAR  =", round(TAR, 3))
        print("TRR  =", round(TRR, 3))
        print("--- System level (FTA = 5%) ---")
        print("FAR  =", round(FAR, 4), "= 0.95 x FMR")
        print("FRR  =", round(FRR, 4), "= 0.05 + 0.95 x FNMR")

        all_results.append([FMR, FNMR, TAR, TRR, FAR, FRR])

    # ---------------- Question 4: comparison table ----------------
    print()
    print("=== COMPARISON TABLE ===")
    print("tau   |  FMR   FNMR   TAR    TRR   |  FAR     FRR")
    for i in range(3):
        r = all_results[i]
        print(thresholds[i], "|", round(r[0], 2), " ", round(r[1], 2), " ",
              round(r[2], 2), " ", round(r[3], 2), " |", round(r[4], 3), " ", round(r[5], 3))

    # ---------------- Plot: effect of the threshold ----------------
    FMR_list = []
    FAR_list = []
    FNMR_list = []
    FRR_list = []
    for r in all_results:
        FMR_list.append(r[0])
        FAR_list.append(r[4])
        FNMR_list.append(r[1])
        FRR_list.append(r[5])

    x = np.arange(3)
    labels = ["0.50", "0.60", "0.70"]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].bar(x - 0.2, FMR_list, 0.4, label="FMR (matcher)")
    axes[0].bar(x + 0.2, FAR_list, 0.4, label="FAR (system)")
    axes[0].set_title("False accepts go DOWN when tau increases")

    axes[1].bar(x - 0.2, FNMR_list, 0.4, label="FNMR (matcher)")
    axes[1].bar(x + 0.2, FRR_list, 0.4, label="FRR (system)")
    axes[1].set_title("False rejects go UP when tau increases")

    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_xlabel("threshold tau")
        ax.set_ylabel("rate")
        ax.legend()
        ax.grid(alpha=0.3)

    fig.savefig("plots/part1/part1_threshold_effect.png", dpi=150)
    plt.close(fig)

    print()
    print("Plots saved in: plots/part1")
