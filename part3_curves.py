import os
import numpy as np
import matplotlib.pyplot as plt

from data import rates


def run():
    os.makedirs("plots/part3", exist_ok=True)

    # ---------------- Question 6: sweep the threshold ----------------
    thresholds = np.round(np.arange(0, 1.001, 0.01), 2)

    FMR_list = []
    FNMR_list = []
    TAR_list = []
    for tau in thresholds:
        FMR, FNMR, TAR, TRR, FAR, FRR = rates(tau)
        FMR_list.append(FMR)
        FNMR_list.append(FNMR)
        TAR_list.append(TAR)

    # ---------------- Question 7: EER ----------------
    # find the smallest difference between FMR and FNMR
    best_diff = 10
    for i in range(len(thresholds)):
        diff = abs(FMR_list[i] - FNMR_list[i])
        if diff < best_diff:
            best_diff = diff

    # all the thresholds that reach this smallest difference
    eer_thresholds = []
    for i in range(len(thresholds)):
        diff = abs(FMR_list[i] - FNMR_list[i])
        if diff < best_diff + 0.000001:
            eer_thresholds.append(thresholds[i])

    eer_tau = (eer_thresholds[0] + eer_thresholds[-1]) / 2
    FMR_eer, FNMR_eer, TAR_eer, TRR_eer, FAR_eer, FRR_eer = rates(eer_thresholds[0])
    EER = (FMR_eer + FNMR_eer) / 2

    print("=== EER ===")
    print("FMR = FNMR for tau from", eer_thresholds[0], "to", eer_thresholds[-1])
    print("Estimated threshold  =", round(eer_tau, 3))
    print("FMR  =", FMR_eer)
    print("FNMR =", FNMR_eer)
    print("EER  =", EER, "(" + str(EER * 100) + " %)")

    # ---------------- Question 8: operating points ----------------
    print()
    print("=== Operating points ===")
    chosen = [("High security", 0.70), ("Convenience", 0.50)]
    for name, tau in chosen:
        FMR, FNMR, TAR, TRR, FAR, FRR = rates(tau)
        print(name, "| tau =", tau, "| FMR =", round(FMR, 3), "| FNMR =", round(FNMR, 3),
              "| FAR =", round(FAR, 3), "| FRR =", round(FRR, 3))

    # ---------------- ROC curve ----------------
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.plot(FMR_list, TAR_list, "b-o", markersize=3, label="ROC curve")

    for name, tau in chosen:
        FMR, FNMR, TAR, TRR, FAR, FRR = rates(tau)
        ax.scatter(FMR, TAR, s=120, zorder=3, label=name + " (tau = " + str(tau) + ")")
    ax.scatter(FMR_eer, TAR_eer, s=120, marker="*", color="red", zorder=3,
               label="EER point (tau = " + str(round(eer_tau, 2)) + ")")

    ax.set_xlabel("FMR")
    ax.set_ylabel("TAR")
    ax.set_title("ROC curve (FMR vs TAR)")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right")
    fig.savefig("plots/part3/part3_roc.png", dpi=150)
    plt.close(fig)

    # ---------------- DET curve ----------------
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.plot(FMR_list, FNMR_list, "b-o", markersize=3, label="DET curve")
    ax.plot([0, 1], [0, 1], "k--", label="FMR = FNMR line")

    for name, tau in chosen:
        FMR, FNMR, TAR, TRR, FAR, FRR = rates(tau)
        ax.scatter(FMR, FNMR, s=120, zorder=3, label=name + " (tau = " + str(tau) + ")")
    ax.scatter(FMR_eer, FNMR_eer, s=120, marker="*", color="red", zorder=3,
               label="EER = " + str(EER))

    ax.set_xlabel("FMR")
    ax.set_ylabel("FNMR")
    ax.set_title("DET curve (FMR vs FNMR)")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right")
    fig.savefig("plots/part3/part3_det.png", dpi=150)
    plt.close(fig)

    # ---------------- FMR and FNMR against the threshold ----------------
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(thresholds, FMR_list, "r-", label="FMR")
    ax.plot(thresholds, FNMR_list, "g-", label="FNMR")
    ax.axvline(eer_tau, color="black", linestyle="--", label="EER threshold")
    ax.set_xlabel("threshold tau")
    ax.set_ylabel("rate")
    ax.set_title("FMR and FNMR against the threshold")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.savefig("plots/part3/part3_fmr_fnmr_vs_threshold.png", dpi=150)
    plt.close(fig)

    print()
    print("Plots saved in: plots/part3")
